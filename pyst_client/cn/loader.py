import asyncio
import zipfile
from itertools import repeat
from pathlib import Path
from urllib.parse import urljoin, quote_plus

import httpx
import orjson
import structlog
from platformdirs import user_data_dir
from rdflib import URIRef
from rdflib.namespace import SKOS
from tqdm import tqdm

from pyst_client.cn.rdf import CombinedNomenclature

logger = structlog.get_logger("sentier_vocab")
transport = httpx.AsyncHTTPTransport(retries=5)

SAMPLE_CORRESPONDENCE_BY_YEAR = {
    2024: [
        URIRef("http://data.europa.eu/xsp/cn2024/CN2024_CN2023_FULL"),
        URIRef("http://data.europa.eu/xsp/cn2024/CN2024_PRODCOM2024"),
    ],
    2025: [
        URIRef("http://data.europa.eu/xsp/cn2025/CN2025_CN2024_FULL"),
        URIRef("http://data.europa.eu/xsp/cn2025/CN2025_CPA22"),
    ],
}


class CombinedNomenclatureLoader:
    def __init__(
        self, year: int, api_key: str, host: str = "http://localhost:8000", sample: bool = False
    ):
        self.year = year
        self.api_key = api_key
        self.host = host
        self.sample = sample

        self.data_dir = Path(user_data_dir("sentier.dev", "dds")) / "vocab-cache"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.filepath = self.download_cn()

        logger.info("Loading RDF graph")
        zf = zipfile.ZipFile(self.filepath, "r")
        self.cn = CombinedNomenclature(zf.open(f"CN_{year}.rdf"), year)

    def download_cn(self) -> Path:
        filepath = self.data_dir / f"CN_{self.year}.rdf.zip"
        if filepath.is_file():
            logger.info(f"Using cached CN {self.year} file")
            return filepath

        url = f"https://showvoc.op.europa.eu/semanticturkey/it.uniroma2.art.semanticturkey/st-core-services/Download/getFile?fileName=CN_{self.year}.zip&ctx_project=ESTAT_Combined_Nomenclature%2C_{self.year}_(CN_{self.year})&"
        logger.info(f"Downloading CN {self.year} from SHOWVOC")
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://showvoc.op.europa.eu/",
            "Cookie": "translate.lang=en",
        }
        with (
            httpx.stream("GET", url, headers=headers, timeout=180) as response,
            open(filepath, "wb") as out_file,
        ):
            if response.status_code != 200:
                raise httpx.HTTPStatusError(
                    f"URL '{url}'' returns status code {response.status_code}."
                )

            for chunk in response.iter_bytes(128 * 1024):
                out_file.write(chunk)

        return filepath

    def write(self) -> None:
        data = self.cn.expanded_json_ld_graph(self.cn.concept_scheme())[0]
        iri = orjson.loads(data)["@id"]
        logger.info("Adding concept scheme")
        asyncio.run(self._request(data=data, url_component="/api/v1/concept_schemes/", url_iri=iri))

        logger.info("Adding concepts")
        data = self.cn.expanded_json_ld_graph(self.cn.concepts(sample=self.sample))
        iris = [orjson.loads(obj)["@id"] for obj in data]
        for ds, iri in tqdm(zip(data, iris)):
            asyncio.run(self._request(data=ds, url_component="/api/v1/concepts/", url_iri=iri))

        data = self.cn.expanded_separate_json_ld_graph(
            SKOS.broader,
            self.cn.relationships(kind=SKOS.broader, sample=self.sample),
        )
        logger.info("Adding skos:broader relationships")
        for elem in tqdm(data):
            asyncio.run(self._request(data=elem, url_component="/api/v1/relationships/"))

        data = self.cn.expanded_separate_json_ld_graph(
            SKOS.relatedMatch,
            self.cn.relationships(kind=SKOS.relatedMatch, sample=self.sample),
        )
        increment = 50
        logger.info("Adding skos:related relationships")
        for index in tqdm(range(0, len(data), increment)):
            asyncio.run(
                self._chunked_request(
                    data=data[index : index + increment], url_component="/api/v1/relationships/"
                )
            )

        if self.sample:
            correspondence_uris = SAMPLE_CORRESPONDENCE_BY_YEAR[self.year]
        else:
            correspondence_uris = self.cn.correspondences()

        logger.info("Adding `Correspondence`")
        for uri in correspondence_uris:
            data = self.cn.expanded_json_ld_graph(
                self.cn.correspondence(uri=uri, sample=self.sample)
            )[0]
            iri = orjson.loads(data)["@id"]
            asyncio.run(self._request(data=data, url_component="/api/v1/correspondences/", url_iri=iri))

        data = [
            self.cn.expanded_json_ld_graph(obj)[0]
            for correspondence in correspondence_uris
            for obj in self.cn.associations(correspondence, sample=self.sample).values()
        ]
        increment = 50
        logger.info("Adding xkos:ConceptAssociations")
        for index in tqdm(range(0, len(data), increment)):
            iris = [orjson.loads(obj)["@id"] for obj in data[index : index + increment]]
            asyncio.run(
                self._chunked_request(
                    data=data[index : index + increment], url_component="/api/v1/associations/", url_iris=iris
                )
            )

        logger.info("Updating `Correspondence:made_of`")
        for uri in correspondence_uris:
            data = self.cn.expanded_json_ld_graph(self.cn.made_of(uri=uri, sample=self.sample))[0]
            asyncio.run(self._request(data=data, url_component="/api/v1/made_ofs/"))

    async def _request(self, url_component: str, data: bytes, url_iri: str | None = None) -> httpx.Response:
        async with httpx.AsyncClient(transport=transport) as client:
            if not isinstance(data, bytes):
                raise TypeError

            response = await client.post(
                urljoin(self.host, url_component + quote_plus(url_iri or "")),
                headers={"X-PyST-Auth-Token": self.api_key, "Content-Type": "application/json"},
                content=data,
            )

        return response

    async def _chunked_request(self, url_component: str, data: list[bytes], url_iris: list[str] | None = None) -> list[httpx.Response]:
        if url_iris is None:
            url_iris = repeat("")

        async with httpx.AsyncClient(transport=transport) as client:
            tasks = []
            for chunk, iri in zip(data, url_iris):
                tasks.append(
                    asyncio.create_task(
                        client.post(
                            urljoin(self.host, url_component + quote_plus(iri)),
                            headers={
                                "X-PyST-Auth-Token": self.api_key,
                                "Content-Type": "application/json",
                            },
                            content=chunk,
                            timeout=120.0,
                        )
                    )
                )
            responses = await asyncio.gather(*tasks)

        return responses
