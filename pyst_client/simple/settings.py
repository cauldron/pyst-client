import functools
from pathlib import Path

import platformdirs
import rfc3987
import structlog
from py_semantic_taxonomy.adapters.routers.validation import validate_iri
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = structlog.get_logger("pyst-client")
base_dir = Path(platformdirs.user_data_dir(appname="PyST-Client", appauthor="cauldron"))
secrets_dir = base_dir / "secrets"
secrets_dir.mkdir(exist_ok=True, parents=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        secrets_dir=secrets_dir,
        env_prefix="PyST_client_",
    )

    api_key: str | None = None
    server_url: str | None = None
    creator: str | None = None
    default_language: str | None = None
    creation_base_url: str | None = None

    def _set(self, key: str, value: str) -> None:
        with open(secrets_dir / f"PyST_client_{key}", "w", encoding="utf-8") as f:
            f.write(value)
        setattr(self, key, value)

    def set_api_key(self, value: str) -> None:
        self._set("api_key", value)

    def set_language(self, value: str) -> None:
        self._set("default_language", value)

    def set_creation_base_url(self, value: str) -> None:
        validate_iri(value)
        self._set("creation_base_url", value)

    def set_server_url(self, value: str) -> None:
        rfc3987.parse(value, rule="absolute_URI")
        self._set("server_url", value)

    def set_creator(self, value: str) -> None:
        validate_iri(value)
        self._set("creator", value)

    def check_read_settings(self) -> None:
        if url := self.server_url:
            logger.info("Server URL %s successfully loaded from secrets directory", url)
        else:
            logger.warning(
                "Server URL not found, no API operations possible. Set with `settings.set_server_url(<something>)`."
            )

        if lang := self.default_language:
            logger.info(
                "Default language `%s` successfully loaded from secrets directory", lang
            )
        else:
            self.set_language("en")
            logger.info(
                "Setting default language to 'en'. Change with `settings.set_language(<something>)`"
            )

    def check_write_settings(self) -> None:
        if self.api_key:
            logger.info("API key successfully loaded from secrets directory")
        else:
            logger.warning(
                "API key not found, write operations impossible. Set with `settings.set_api_key(<something>)`."
            )

        if self.creation_base_url:
            logger.info("Creation base URL successfully loaded from secrets directory")
        else:
            logger.warning(
                "Creation base URL not found, write operations impossible. Set with `settings.set_creation_base_url(<something>)`."
            )


settings = Settings()


def can_write(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
        if not settings.server_url:
            raise ValueError("Server URL is missing but required for this function.")
        if not settings.creator:
            raise ValueError(
                "Creator setting is missing but required for this function."
            )
        if not settings.api_key:
            raise ValueError("API key is missing but required for this function.")
        if not settings.creation_base_url:
            raise ValueError(
                "Creation base URL is missing but required for this function."
            )
        return func(self, *args, **kwargs)

    return wrap
