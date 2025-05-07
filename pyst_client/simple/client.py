import functools
from urllib.parse import urljoin

import httpx
import structlog
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.settings import settings

logger = structlog.get_logger("pyst-client")


class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class ReadClient:
    def __init__(self):
        settings.check_read_settings()
        if settings.server_url:
            resp = httpx.get(
                urljoin(settings.server_url, get_full_api_path("status")), timeout=2
            )
            if resp.status_code != 200:
                logger.warning(
                    "Server URL `%s` is reachable but not healthy. Response content: %s",
                    settings.server_url,
                    resp.text,
                )
            else:
                logger.info(
                    "Server URL `%s` is healthy and reachable", settings.server_url
                )

    def server_healthy(self) -> bool:
        resp = httpx.get(
            urljoin(self.settings.server_url, get_full_api_path("status")), timeout=2
        )
        return resp.status_code == 200

    def has_server_config(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if not settings.server_url:
                raise ValueError(
                    "Server URL is missing but required for this function. Set with `client.set_server_url()`."
                )
            return func(self, *args, **kwargs)

        return wrap

    def get(self, *args, **kwargs) -> httpx.Response:
        response = self.client().get(*args, **kwargs)
        self.check_error(response)
        return response

    def client(self) -> httpx.Client:
        return httpx.Client(
            base_url=settings.server_url,
            headers={
                "Content-Type": "application/json",
                "x-pyst-auth-token": settings.api_key,
            },
        )

    def check_error(self, response: httpx.Response) -> None:
        if response.status_code not in (200, 204):
            try:
                error = response.json()
            except:
                error = response.text
            raise APIError(str(error), status_code=response.status_code)


class WriteClient(ReadClient):
    def __init__(self):
        super().__init__()
        settings.check_write_settings()

    def has_server_config(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if not self.settings.server_url:
                raise ValueError(
                    "Server URL is missing but required for this function."
                )
            if not self.settings.creator:
                raise ValueError(
                    "Creator setting is missing but required for this function."
                )
            if not self.settings.api_key:
                raise ValueError("API key is missing but required for this function.")
            if not self.settings.creation_base_url:
                raise ValueError(
                    "Creation base URL is missing but required for this function."
                )
            return func(self, *args, **kwargs)

        return wrap

    def post(self, *args, **kwargs) -> httpx.Response:
        response = self.client().post(*args, **kwargs)
        self.check_error(response)
        return response

    def put(self, *args, **kwargs) -> httpx.Response:
        response = self.client().put(*args, **kwargs)
        self.check_error(response)
        return response

    def delete(self, *args, **kwargs) -> httpx.Response:
        response = self.client().delete(*args, **kwargs)
        self.check_error(response)
        return response


@functools.lru_cache(maxsize=1)
def get_read_client():
    return ReadClient()


@functools.lru_cache(maxsize=1)
def get_write_client():
    return WriteClient()
