import datetime
from urllib.parse import quote

import orjson
from py_semantic_taxonomy.adapters.routers import request_dto as req
from py_semantic_taxonomy.adapters.routers.validation import (
    DateTime,
    DateTimeType,
    MultilingualString,
    Notation,
    Status,
    StatusChoice,
)
from py_semantic_taxonomy.domain import entities
from py_semantic_taxonomy.domain.constants import SKOS, AssociationKind
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.classes.api_base import APIBase
from pyst_client.simple.classes.concept_scheme import ConceptScheme
from pyst_client.simple.settings import can_write, settings


class Concept(entities.Concept, APIBase):
    @property
    def api_path(self) -> str:
        return get_full_api_path("concept", iri=self.id_)

    @property
    def web_path(self) -> str:
        return (
            "web/concept/"
            + quote(self.id_, safe="")
            + "?language="
            + settings.default_language
        )

    @classmethod
    def get_one(
        cls,
        iri: str,
        timeout: int = 5,
    ) -> "Concept":
        return cls.from_json_ld(
            orjson.loads(cls._get_one("concept", iri, timeout=timeout).text)
        )

    @classmethod
    def get_many(
        cls,
        concept_scheme_iri: str | None = None,
        top_concepts_only: bool = False,
        timeout: int = 5,
    ) -> list["Concept"]:
        return [
            cls.from_json_ld(obj)
            for obj in orjson.loads(
                cls._get_many(
                    "concept_all",
                    params={
                        "concept_scheme_iri": concept_scheme_iri,
                        "top_concepts_only": top_concepts_only,
                    },
                    timeout=timeout,
                ).text
            )
        ]

    @classmethod
    @can_write
    def generate_iri(
        cls, *, concept_scheme: ConceptScheme, notations: list[str | Notation] = []
    ):
        if not concept_scheme.notations:
            raise ValueError(
                "No concept scheme `notations` provided; automatic id generation requires the at least one concept scheme notation"
            )
        if not notations:
            raise ValueError(
                "No `notations` provided; automatic id generation requires at least one concept notation"
            )
        return "{}{}{}/{}".format(
            settings.creation_base_url,
            "" if settings.creation_base_url.endswith("/") else "/",
            concept_scheme.notations[0]["@value"],
            notations[0],
        )

    @classmethod
    @can_write
    def create(
        cls,
        *,
        concept_scheme: ConceptScheme,
        pref_labels: list[str | MultilingualString],
        alt_labels: list[str | MultilingualString] = [],
        hidden_labels: list[str | MultilingualString] = [],
        notations: list[str | Notation] = [],
        definitions: list[str | MultilingualString] = [],
        status: Status = Status(**{"@id": StatusChoice.accepted}),
        top_concept: bool = False,
        extra: dict | None = None,
        creation_message: str | None = None,
        id_: str | None = None,
    ) -> "Concept":
        if id_ is None:
            id_ = cls.generate_iri(concept_scheme=concept_scheme, notations=notations)

        concept = cls(
            id_=id_,
            schemes=[{"@id": concept_scheme.id_}],
            types=[f"{SKOS}Concept"],
            status=[status.model_dump(by_alias=True)],
            notations=[
                (
                    Notation(**{"@value": obj}) if isinstance(obj, str) else obj
                ).model_dump(by_alias=True)
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
            alt_labels=[
                (
                    {"@value": obj, "@language": settings.default_language}
                    if isinstance(obj, str)
                    else obj.model_dump(by_alias=True)
                )
                for obj in alt_labels
            ],
            hidden_labels=[
                (
                    {"@value": obj, "@language": settings.default_language}
                    if isinstance(obj, str)
                    else obj.model_dump(by_alias=True)
                )
                for obj in hidden_labels
            ],
            definitions=[
                (
                    {"@value": obj, "@language": settings.default_language}
                    if isinstance(obj, str)
                    else obj.model_dump(by_alias=True)
                )
                for obj in definitions
            ],
            top_concept_of=[{"@id": concept_scheme.id_}] if top_concept else [],
            extra={} if extra is None else extra,
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
        )
        req.Concept(**concept.to_json_ld())
        return concept

    def relationships(
        self, source: bool = True, target: bool = False, timeout: int = 5
    ) -> list:
        from pyst_client.simple.classes.relationship import Relationship

        return Relationship.get_many(concept=self, source=source, target=target)

    def associations(
        self,
        correspondence=None,
        source: bool = True,
        target: bool = False,
        kind: AssociationKind | None = None,
        timeout: int = 5,
    ) -> list:
        from pyst_client.simple.classes.association import Association

        results = []
        if source:
            results.extend(
                Association.get_many(
                    correspondence=correspondence,
                    source_concept=self,
                    kind=kind,
                    timeout=timeout,
                )
            )
        if target:
            results.extend(
                Association.get_many(
                    correspondence=correspondence,
                    target_concept=self,
                    kind=kind,
                    timeout=timeout,
                )
            )
        return results
