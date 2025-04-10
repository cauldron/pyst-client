import asyncio
import zipfile
from pathlib import Path
from urllib.parse import urljoin

import httpx
import structlog
from platformdirs import user_data_dir
from rdflib import URIRef
from rdflib.namespace import SKOS
from tqdm import tqdm

from pyst_client.cn.rdf import CombinedNomenclature

logger = structlog.get_logger("sentier_vocab")


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
        logger.info("Adding concept scheme")
        asyncio.run(self._request(data=data, url_component="/concept_scheme/"))

        data = self.cn.expanded_json_ld_graph(self.cn.concepts(sample=self.sample))
        increment = 20
        logger.info("Adding concepts")
        for index in tqdm(range(0, len(data), increment)):
            asyncio.run(self._chunked_request(url_component="/concept/", data=data))

        data = self.cn.expanded_separate_json_ld_graph(
            SKOS.broader,
            self.cn.relationships(kind=SKOS.broader, sample=self.sample),
        )
        logger.info("Adding skos:broader relationships")
        asyncio.run(self._chunked_request(data=data, url_component="/relationships/"))

        data = self.cn.expanded_separate_json_ld_graph(
            SKOS.relatedMatch,
            self.cn.relationships(kind=SKOS.relatedMatch, sample=self.sample),
        )
        increment = 50
        logger.info("Adding skos:related relationships")
        for index in tqdm(range(0, len(data), increment)):
            asyncio.run(
                self._chunked_request(
                    data=data[index : index + increment], url_component="/relationships/"
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
            asyncio.run(self._request(data=data, url_component="/correspondence/"))

        data = [
            self.cn.expanded_json_ld_graph(obj)[0]
            for correspondence in correspondence_uris
            for obj in self.cn.associations(correspondence, sample=self.sample).values()
        ]
        increment = 50
        logger.info("Adding xkos:ConceptAssociations")
        for index in tqdm(range(0, len(data), increment)):
            asyncio.run(
                self._chunked_request(
                    data=data[index : index + increment], url_component="/association/"
                )
            )

        logger.info("Updating `Correspondence:made_of`")
        for uri in correspondence_uris:
            data = self.cn.expanded_json_ld_graph(self.cn.made_of(uri=uri, sample=self.sample))[0]
            asyncio.run(self._request(data=data, url_component="/made_of/"))

    async def _request(self, url_component: str, data: bytes) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            if not isinstance(data, bytes):
                raise TypeError

            response = await client.post(
                urljoin(self.host, url_component),
                headers={"X-PyST-Auth-Token": self.api_key, "Content-Type": "application/json"},
                content=data,
            )

        return response

    async def _chunked_request(self, url_component: str, data: list[bytes]) -> list[httpx.Response]:
        async with httpx.AsyncClient() as client:
            tasks = []
            for chunk in data:
                tasks.append(
                    asyncio.create_task(
                        client.post(
                            urljoin(self.host, url_component),
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
