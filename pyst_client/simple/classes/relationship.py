import itertools

import orjson
import structlog
from py_semantic_taxonomy.adapters.routers import request_dto as req
from py_semantic_taxonomy.domain import entities
from py_semantic_taxonomy.domain.constants import RelationshipVerbs
from py_semantic_taxonomy.domain.url_utils import get_full_api_path

from pyst_client.simple.classes.concept import Concept
from pyst_client.simple.client import APIError, get_read_client, get_write_client
from pyst_client.simple.settings import can_write

logger = structlog.get_logger("pyst-client")


class Relationship(entities.Relationship):
    @classmethod
    def get_many(
        cls,
        concept: Concept | str,
        source: bool = True,
        target: bool = False,
        timeout: int = 5,
    ) -> list["Concept"]:
        return [
            cls.from_json_ld(obj)
            for obj in orjson.loads(
                get_read_client()
                .get(
                    get_full_api_path("relationship"),
                    params={
                        "iri": concept.id_ if isinstance(concept, Concept) else concept,
                        "source": source,
                        "target": target,
                    },
                    timeout=timeout,
                )
                .text
            )
        ]

    @classmethod
    @can_write
    def create_many(
        cls,
        *,
        sources: list[Concept | str],
        targets: list[Concept | str],
        verbs: list[RelationshipVerbs] | RelationshipVerbs,
        timeout: int = 120,
        skip_duplicates: bool = True,
    ) -> list:
        if isinstance(verbs, RelationshipVerbs):
            verbs = itertools.repeat(verbs)

        relationships = [
            cls(
                source=getattr(source, "id_", source),
                target=getattr(target, "id_", target),
                predicate=verb,
            )
            for source, target, verb in zip(sources, targets, verbs)
        ]
        # Validation
        [req.Relationship(**obj.to_json_ld()) for obj in relationships]

        errors = True
        while errors:
            try:
                get_write_client().post(
                    get_full_api_path("relationship"),
                    data=orjson.dumps([obj.to_json_ld() for obj in relationships]),
                    timeout=timeout,
                )
                errors = False
            except APIError as err:
                if err.status_code != 409 or not skip_duplicates:
                    raise err
                relationships = remove_duplicates(data=relationships, message=str(err))
        return relationships

    @classmethod
    @can_write
    def delete_many(
        cls,
        *,
        sources: list[Concept | str],
        targets: list[Concept | str],
        verbs: list[RelationshipVerbs] | RelationshipVerbs,
    ) -> list:
        if isinstance(verbs, RelationshipVerbs):
            verbs = itertools.repeat(verbs)

        relationships = [
            cls(
                source=getattr(source, "id_", source),
                target=getattr(target, "id_", target),
                predicate=verb,
            )
            for source, target, verb in zip(sources, targets, verbs)
        ]
        # Validation
        [req.Relationship(**obj.to_json_ld()) for obj in relationships]
        get_write_client().client().request(
            url=get_full_api_path("relationship"),
            method="delete",
            content=orjson.dumps([obj.to_json_ld() for obj in relationships]),
        )
        return relationships


def remove_duplicates(data: list[Relationship], message: str) -> list[Relationship]:
    first = "Relationship between source `"
    second = "` and target `"
    third = "` already exists"

    source = message[message.index(first) + len(first) : message.index(second)]
    target = message[message.index(second) + len(second) : message.index(third)]

    logger.info("Skipping existing relationship between `%s` and `%s`", source, target)
    return [obj for obj in data if obj.source != source and obj.target != target]
