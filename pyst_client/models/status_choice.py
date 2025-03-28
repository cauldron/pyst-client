# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StatusChoice(str, Enum):
    """
    StatusChoice
    """

    """
    allowed enum values
    """
    HTTP_COLON_SLASH_SLASH_PURL_DOT_ORG_SLASH_ONTOLOGY_SLASH_BIBO_SLASH_STATUS_SLASH_ACCEPTED = 'http://purl.org/ontology/bibo/status/accepted'
    HTTP_COLON_SLASH_SLASH_PURL_DOT_ORG_SLASH_ONTOLOGY_SLASH_BIBO_SLASH_STATUS_SLASH_DRAFT = 'http://purl.org/ontology/bibo/status/draft'
    HTTP_COLON_SLASH_SLASH_PURL_DOT_ORG_SLASH_ONTOLOGY_SLASH_BIBO_SLASH_STATUS_SLASH_REJECTED = 'http://purl.org/ontology/bibo/status/rejected'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusChoice from a JSON string"""
        return cls(json.loads(json_str))


