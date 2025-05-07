import datetime

import orjson
from py_semantic_taxonomy.adapters.routers import request_dto as req
from py_semantic_taxonomy.adapters.routers.validation import (
    DateTime,
    DateTimeType,
    MultilingualString,
    Notation,
    Status,
    StatusChoice,
    VersionString,
)
from py_semantic_taxonomy.domain import entities
from py_semantic_taxonomy.domain.constants import XKOS
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.classes.api_base import APIBase
from pyst_client.simple.classes.concept_scheme import ConceptScheme
from pyst_client.simple.settings import can_write, settings


class Correspondence(entities.Correspondence, APIBase):
    @property
    def api_path(self) -> str:
        return get_full_api_path("correspondence", iri=self.id_)

    def open_new_tab(self) -> None:
        raise NotImplementedError

    @classmethod
    def get_one(
        cls,
        iri: str,
        timeout: int = 5,
    ) -> "Correspondence":
        return cls.from_json_ld(
            orjson.loads(cls._get_one("correspondence", iri, timeout=timeout).text)
        )

    @classmethod
    def get_many(
        cls,
        timeout: int = 5,
    ) -> list["Correspondence"]:
        return [
            cls.from_json_ld(obj)
            for obj in orjson.loads(
                cls._get_many("correspondence_all", timeout=timeout).text
            )
        ]

    @classmethod
    @can_write
    def create(
        cls,
        *,
        pref_labels: list[str | MultilingualString],
        compares: list[ConceptScheme],
        version: str | VersionString = "1.0",
        status: Status = Status(**{"@id": StatusChoice.accepted}),
        notations: list[str | Notation] = [],
        creation_message: str | None = None,
        definitions: list[str | MultilingualString] = [],
        id_: str | None = None,
        extra: dict | None = None,
        creators: list[dict] = [],
    ) -> "Correspondence":
        if not notations:
            notations = ["-".join([cs.notations[0]["@value"] for cs in compares])]
        if id_ is None:
            id_ = "{}{}{}".format(
                settings.creation_base_url,
                "" if settings.creation_base_url.endswith("/") else "/",
                notations[0],
            )
        if isinstance(version, str):
            version = [VersionString(**{"@value": version}).model_dump(by_alias=True)]
        if not creators:
            creators = [{"@id": settings.creator}]

        scheme = cls(
            id_=id_,
            compares=[{"@id": obj.id_} for obj in compares],
            types=[f"{XKOS}Correspondence"],
            status=[status.model_dump(by_alias=True)],
            notations=[
                Notation(**{"@value": obj} if isinstance(obj, str) else obj).model_dump(
                    by_alias=True
                )
                for obj in notations
            ],
            pref_labels=[
                (
                    {"@value": obj, "@language": settings.default_language}
                    if isinstance(obj, str)
                    else obj.model_dump(by_alias=True)
                )
                for obj in pref_labels
            ],
            definitions=[
                (
                    {"@value": obj, "@language": settings.default_language}
                    if isinstance(obj, str)
                    else obj.model_dump(by_alias=True)
                )
                for obj in definitions
            ],
            extra=extra or {},
            history_notes=[
                {
                    "http://www.w3.org/1999/02/22-rdf-syntax-ns#value": [
                        {
                            "@language": (
                                "en"
                                if not creation_message
                                else settings.default_language
                            ),
                            "@value": creation_message
                            or "Created by pyst-client version 1",
                        }
                    ],
                    "http://purl.org/dc/terms/creator": [{"@id": settings.creator}],
                    "http://purl.org/dc/terms/issued": [
                        DateTime(
                            **{
                                "@type": DateTimeType.date,
                                "@value": datetime.date.today(),
                            }
                        ).model_dump(by_alias=True)
                    ],
                }
            ],
            creators=creators,
            version=version,
            created=[
                DateTime(
                    **{"@type": DateTimeType.date, "@value": datetime.date.today()}
                ).model_dump(by_alias=True)
            ],
        )
        req.Correspondence(**scheme.to_json_ld())
        return scheme
