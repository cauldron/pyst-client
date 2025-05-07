import uuid

import orjson
import structlog
from py_semantic_taxonomy.adapters.routers import request_dto as req
from py_semantic_taxonomy.domain import entities
from py_semantic_taxonomy.domain.constants import XKOS, AssociationKind
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.classes.api_base import APIBase
from pyst_client.simple.classes.concept import Concept
from pyst_client.simple.classes.correspondence import Correspondence
from pyst_client.simple.client import get_write_client
from pyst_client.simple.settings import can_write, settings

logger = structlog.get_logger("pyst-client")


class Association(entities.Association, APIBase):
    def open_new_tab(self) -> None:
        raise NotImplementedError

    @property
    def api_path(self) -> str:
        return get_full_api_path("association", iri=self.id_)

    @classmethod
    def get_one(
        cls,
        iri: str,
        timeout: int = 5,
    ) -> "Association":
        return cls.from_json_ld(
            orjson.loads(cls._get_one("association", iri, timeout=timeout).text)
        )

    @classmethod
    def get_many(
        cls,
        correspondence: Correspondence | str | None = None,
        source_concept: Concept | str | None = None,
        target_concept: Concept | str | None = None,
        kind: AssociationKind | None = None,
        timeout: int = 5,
    ) -> list["Concept"]:
        params = {
            "correspondence_iri": (
                correspondence.id_
                if isinstance(correspondence, Correspondence)
                else correspondence
            ),
            "source_concept_iri": (
                source_concept.id_
                if isinstance(source_concept, Concept)
                else source_concept
            ),
            "target_concept_iri": (
                target_concept.id_
                if isinstance(target_concept, Concept)
                else target_concept
            ),
            "kind": kind or AssociationKind.simple,
        }
        return [
            cls.from_json_ld(obj)
            for obj in orjson.loads(
                cls._get_many(
                    "association_all",
                    params={
                        key: value for key, value in params.items() if value is not None
                    },
                    timeout=timeout,
                ).text
            )
        ]

    @classmethod
    @can_write
    def create(
        cls,
        *,
        correspondence: Correspondence,
        source_concepts: list[Concept | dict],
        target_concepts: list[Concept | dict],
        extra: dict | None = None,
        id_: str | None = None,
    ) -> "Concept":
        if id_ is None:
            id_ = "{}{}{}/{}".format(
                settings.creation_base_url,
                "" if settings.creation_base_url.endswith("/") else "/",
                correspondence.notations[0]["@value"],
                uuid.uuid4().hex,
            )
        extra = extra or {}
        extra[f"{XKOS}Correspondence"] = correspondence.id_
        assoc = cls(
            id_=id_,
            types=[f"{XKOS}ConceptAssociation"],
            source_concepts=[
                ({"@id": obj.id_} if isinstance(obj, Concept) else obj)
                for obj in source_concepts
            ],
            target_concepts=[
                ({"@id": obj.id_} if isinstance(obj, Concept) else obj)
                for obj in target_concepts
            ],
            kind=(
                AssociationKind.simple
                if len(source_concepts) == 1
                else AssociationKind.conditional
            ),
            extra=extra or {},
        )
        req.Association(**assoc.to_json_ld())
        return assoc

    def save(self) -> None:
        client = get_write_client()
        client.post(
            self.api_path,
            data=self.json(),
        )
        # Add association to correspondence
        if f"{XKOS}Correspondence" in self.extra:
            client.post(
                get_full_api_path("made_of"),
                data=orjson.dumps(
                    entities.MadeOf(
                        id_=self.extra[f"{XKOS}Correspondence"],
                        made_ofs=[{"@id": self.id_}],
                    ).to_json_ld()
                ),
            )
        else:
            logger.warning(
                "Unable to automatically add this association to a `Correspondence` object"
            )

    def delete(self) -> None:
        client = get_write_client()
        return client.delete(
            self.api_path,
        )
        if f"{XKOS}Correspondence" in self.extra:
            client.request(
                url=get_full_api_path("made_of"),
                method="DELETE",
                content=orjson.dumps(
                    entities.MadeOf(
                        id_=self.extra[f"{XKOS}Correspondence"],
                        made_ofs=[{"@id": self.id_}],
                    ).to_json_ld()
                ),
            )
        else:
            logger.warning(
                "Unable to automatically remove this association from a `Correspondence` object"
            )
