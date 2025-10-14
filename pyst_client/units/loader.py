import asyncio
from itertools import repeat
from urllib.parse import quote_plus, urljoin
from pprint import pprint

import httpx
import structlog
from tqdm import tqdm

from pyst_client.units.errors import QUDTLoaderHTTPError
from pyst_client.units.rdf import QUDT, HEALTHY_RELATIONSHIPS
from pyst_client.units.utils import async_request


logger = structlog.get_logger("sentier_vocab")
transport = httpx.AsyncHTTPTransport(retries=5)


class QUDTLoader:
    def __init__(self, api_key: str, host: str = "http://localhost:8000", ignore_422_errors: bool = False):
        self.api_key = api_key
        self.host = host
        self.ignore_422_errors = ignore_422_errors

        logger.info("Loading RDF graph")
        self.qudt = QUDT()

    def write(self) -> None:
        data = self.qudt.expanded_json_ld_graph(self.qudt.concept_scheme())[0]
        iri = orjson.loads(data)["@id"]
        logger.info("Adding concept scheme")
        asyncio.run(self._request(data=data, url_component="/api/v1/concept_schemes/", url_iri=iri))

        logger.info("Adding concepts")
        data = self.qudt.expanded_json_ld_graph(self.qudt.concepts())
        iris = [orjson.loads(obj)["@id"] for obj in data]
        for ds, iri in tqdm(list(zip(data, iris))):
            asyncio.run(
                self._request(data=ds, url_component="/api/v1/concepts/", url_iri=iri)
            )

        for relationship in HEALTHY_RELATIONSHIPS:
            logger.info(f"Adding {relationship} relationships")
            data = self.qudt.expanded_separate_json_ld_graph(
                relationship,
                self.qudt.relationships(kind=relationship),
            )
            for elem in tqdm(data):
                asyncio.run(async_request(data=elem, url_component="/api/v1/relationships/"), host=self.host, api_key=self.api_key, ignore_422_errors=self.ignore_422_errors)

        # correspondence_uris = self.qudt.correspondences()

        # logger.info("Adding `Correspondence`")
        # for uri in correspondence_uris:
        #     data = self.qudt.expanded_json_ld_graph(
        #         self.qudt.correspondence(uri=uri, sample=self.sample)
        #     )[0]
        #     iri = orjson.loads(data)["@id"]
        #     asyncio.run(self._request(data=data, url_component="/api/v1/correspondences/", url_iri=iri))

        # data = [
        #     self.qudt.expanded_json_ld_graph(obj)[0]
        #     for correspondence in correspondence_uris
        #     for obj in self.qudt.associations(correspondence, sample=self.sample).values()
        # ]
        # increment = 50
        # logger.info("Adding xkos:ConceptAssociations")
        # for index in tqdm(range(0, len(data), increment)):
        #     iris = [orjson.loads(obj)["@id"] for obj in data[index : index + increment]]
        #     asyncio.run(
        #         self._chunked_request(
        #             data=data[index : index + increment], url_component="/api/v1/associations/", url_iris=iris
        #         )
        #     )

        # logger.info("Updating `Correspondence:made_of`")
        # for uri in correspondence_uris:
        #     data = self.qudt.expanded_json_ld_graph(self.qudt.made_of(uri=uri, sample=self.sample))[0]
        #     asyncio.run(self._request(data=data, url_component="/api/v1/made_ofs/"))

    async def _chunked_request(
        self, url_component: str, data: list[bytes], url_iris: list[str] | None = None
    ) -> list[httpx.Response]:
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

            # Check for HTTP errors in responses, but don't raise on 409 Conflict (duplicate resource)
            # Optionally ignore 422 Unprocessable Entity based on flag
            ignored_codes = {409}
            if self.ignore_422_errors:
                ignored_codes.add(422)
            
            for i, response in enumerate(responses):
                if response.status_code >= 400 and response.status_code not in ignored_codes:
                    try:
                        response_text = response.text
                    except Exception:
                        response_text = "Unable to decode response text"

                    iri = list(url_iris)[i] if i < len(list(url_iris)) else "unknown"
                    error_message = (
                        f"HTTP request failed with status {response.status_code}"
                    )
                    if iri:
                        error_message += f" for resource: {iri}"

                    pprint(response.json())
                    raise QUDTLoaderHTTPError(
                        message=error_message,
                        status_code=response.status_code,
                        response_text=response_text,
                    )

        return responses
