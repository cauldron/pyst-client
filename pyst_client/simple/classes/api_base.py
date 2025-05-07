import webbrowser
from urllib.parse import urljoin

import orjson
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.client import APIError, get_read_client, get_write_client
from pyst_client.simple.settings import settings


class APIBase:
    @property
    def api_url(self) -> str:
        return urljoin(settings.server_url, self.api_path)

    @property
    def web_url(self) -> str:
        return urljoin(settings.server_url, self.web_path)

    def open_new_tab(self) -> None:
        webbrowser.open_new_tab(self.web_url)

    def json(self) -> bytes:
        return orjson.dumps(self.to_json_ld())

    def save(self, already_exists: bool = False) -> None:
        client = get_write_client()
        if not already_exists:
            try:
                return client.post(
                    self.api_path,
                    data=self.json(),
                )
            except APIError as err:
                if err.status_code != 409:
                    raise err
        return client.put(
            self.api_path,
            data=[self.json()],
        )

    def delete(self) -> None:
        client = get_write_client()
        return client.delete(
            self.api_path,
        )

    @classmethod
    def _get_many(
        cls,
        url_label: str,
        params: dict = {},
        timeout: int = 5,
    ) -> list[dict]:
        return get_read_client().get(
            get_full_api_path(url_label),
            params=params,
            timeout=timeout,
        )

    @classmethod
    def _get_one(
        cls,
        url_label: str,
        iri: str,
        timeout: int = 5,
    ) -> dict:
        return get_read_client().get(
            get_full_api_path(url_label, iri=iri),
            timeout=timeout,
        )
