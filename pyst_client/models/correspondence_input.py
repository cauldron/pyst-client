# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pyst_client.models.multilingual_string import MultilingualString
from pyst_client.models.node import Node
from pyst_client.models.non_literal_note import NonLiteralNote
from pyst_client.models.notation import Notation
from pyst_client.models.status import Status
from pyst_client.models.version_string import VersionString
from typing import Optional, Set
from typing_extensions import Self

class CorrespondenceInput(BaseModel):
    """
    CorrespondenceInput
    """ # noqa: E501
    id: StrictStr = Field(description="https://www.w3.org/TR/json-ld/#node-identifiers", alias="@id")
    type: List[StrictStr] = Field(description="https://www.w3.org/TR/json-ld/#specifying-the-type", alias="@type")
    http___www_w3_org_2004_02_skos_corepref_label: Annotated[List[MultilingualString], Field(min_length=1)] = Field(description="https://www.w3.org/TR/skos-primer/#secpref", alias="http://www.w3.org/2004/02/skos/core#prefLabel")
    http___purl_org_ontology_bibo_status: Annotated[List[Status], Field(min_length=1)] = Field(description="https://github.com/dcmi/bibo/blob/main/rdf/bibo.ttl#L391", alias="http://purl.org/ontology/bibo/status")
    http___www_w3_org_2004_02_skos_corenotation: Optional[List[Notation]] = Field(default=None, description="https://www.w3.org/TR/skos-primer/#secnotations", alias="http://www.w3.org/2004/02/skos/core#notation")
    http___www_w3_org_2004_02_skos_corechange_note: Optional[List[NonLiteralNote]] = Field(default=None, alias="http://www.w3.org/2004/02/skos/core#changeNote")
    http___www_w3_org_2004_02_skos_corehistory_note: Optional[List[NonLiteralNote]] = Field(default=None, alias="http://www.w3.org/2004/02/skos/core#historyNote")
    http___www_w3_org_2004_02_skos_coreeditorial_note: Optional[List[NonLiteralNote]] = Field(default=None, alias="http://www.w3.org/2004/02/skos/core#editorialNote")
    http___purl_org_dc_terms_created: Annotated[List[datetime], Field(min_length=1, max_length=1)] = Field(description="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/created", alias="http://purl.org/dc/terms/created")
    http___purl_org_dc_terms_creator: List[Node] = Field(description="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/creator", alias="http://purl.org/dc/terms/creator")
    http___www_w3_org_2002_07_owlversion_info: Annotated[List[VersionString], Field(min_length=1, max_length=1)] = Field(description="https://www.w3.org/TR/owl-ref/#versionInfo-def", alias="http://www.w3.org/2002/07/owl#versionInfo")
    http___www_w3_org_2004_02_skos_coredefinition: Optional[List[MultilingualString]] = Field(default=None, description="https://www.w3.org/TR/skos-primer/#secdocumentation", alias="http://www.w3.org/2004/02/skos/core#definition")
    http___rdf_vocabulary_ddialliance_org_xkoscompares: Annotated[List[Node], Field(min_length=1)] = Field(description="https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences", alias="http://rdf-vocabulary.ddialliance.org/xkos#compares")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["@id", "@type", "http://www.w3.org/2004/02/skos/core#prefLabel", "http://purl.org/ontology/bibo/status", "http://www.w3.org/2004/02/skos/core#notation", "http://www.w3.org/2004/02/skos/core#changeNote", "http://www.w3.org/2004/02/skos/core#historyNote", "http://www.w3.org/2004/02/skos/core#editorialNote", "http://purl.org/dc/terms/created", "http://purl.org/dc/terms/creator", "http://www.w3.org/2002/07/owl#versionInfo", "http://www.w3.org/2004/02/skos/core#definition", "http://rdf-vocabulary.ddialliance.org/xkos#compares"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CorrespondenceInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_corepref_label (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_corepref_label:
            for _item_http___www_w3_org_2004_02_skos_corepref_label in self.http___www_w3_org_2004_02_skos_corepref_label:
                if _item_http___www_w3_org_2004_02_skos_corepref_label:
                    _items.append(_item_http___www_w3_org_2004_02_skos_corepref_label.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#prefLabel'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___purl_org_ontology_bibo_status (list)
        _items = []
        if self.http___purl_org_ontology_bibo_status:
            for _item_http___purl_org_ontology_bibo_status in self.http___purl_org_ontology_bibo_status:
                if _item_http___purl_org_ontology_bibo_status:
                    _items.append(_item_http___purl_org_ontology_bibo_status.to_dict())
            _dict['http://purl.org/ontology/bibo/status'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_corenotation (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_corenotation:
            for _item_http___www_w3_org_2004_02_skos_corenotation in self.http___www_w3_org_2004_02_skos_corenotation:
                if _item_http___www_w3_org_2004_02_skos_corenotation:
                    _items.append(_item_http___www_w3_org_2004_02_skos_corenotation.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#notation'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_corechange_note (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_corechange_note:
            for _item_http___www_w3_org_2004_02_skos_corechange_note in self.http___www_w3_org_2004_02_skos_corechange_note:
                if _item_http___www_w3_org_2004_02_skos_corechange_note:
                    _items.append(_item_http___www_w3_org_2004_02_skos_corechange_note.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#changeNote'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_corehistory_note (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_corehistory_note:
            for _item_http___www_w3_org_2004_02_skos_corehistory_note in self.http___www_w3_org_2004_02_skos_corehistory_note:
                if _item_http___www_w3_org_2004_02_skos_corehistory_note:
                    _items.append(_item_http___www_w3_org_2004_02_skos_corehistory_note.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#historyNote'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_coreeditorial_note (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_coreeditorial_note:
            for _item_http___www_w3_org_2004_02_skos_coreeditorial_note in self.http___www_w3_org_2004_02_skos_coreeditorial_note:
                if _item_http___www_w3_org_2004_02_skos_coreeditorial_note:
                    _items.append(_item_http___www_w3_org_2004_02_skos_coreeditorial_note.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#editorialNote'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___purl_org_dc_terms_creator (list)
        _items = []
        if self.http___purl_org_dc_terms_creator:
            for _item_http___purl_org_dc_terms_creator in self.http___purl_org_dc_terms_creator:
                if _item_http___purl_org_dc_terms_creator:
                    _items.append(_item_http___purl_org_dc_terms_creator.to_dict())
            _dict['http://purl.org/dc/terms/creator'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2002_07_owlversion_info (list)
        _items = []
        if self.http___www_w3_org_2002_07_owlversion_info:
            for _item_http___www_w3_org_2002_07_owlversion_info in self.http___www_w3_org_2002_07_owlversion_info:
                if _item_http___www_w3_org_2002_07_owlversion_info:
                    _items.append(_item_http___www_w3_org_2002_07_owlversion_info.to_dict())
            _dict['http://www.w3.org/2002/07/owl#versionInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___www_w3_org_2004_02_skos_coredefinition (list)
        _items = []
        if self.http___www_w3_org_2004_02_skos_coredefinition:
            for _item_http___www_w3_org_2004_02_skos_coredefinition in self.http___www_w3_org_2004_02_skos_coredefinition:
                if _item_http___www_w3_org_2004_02_skos_coredefinition:
                    _items.append(_item_http___www_w3_org_2004_02_skos_coredefinition.to_dict())
            _dict['http://www.w3.org/2004/02/skos/core#definition'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in http___rdf_vocabulary_ddialliance_org_xkoscompares (list)
        _items = []
        if self.http___rdf_vocabulary_ddialliance_org_xkoscompares:
            for _item_http___rdf_vocabulary_ddialliance_org_xkoscompares in self.http___rdf_vocabulary_ddialliance_org_xkoscompares:
                if _item_http___rdf_vocabulary_ddialliance_org_xkoscompares:
                    _items.append(_item_http___rdf_vocabulary_ddialliance_org_xkoscompares.to_dict())
            _dict['http://rdf-vocabulary.ddialliance.org/xkos#compares'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CorrespondenceInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "http://www.w3.org/2004/02/skos/core#prefLabel": [MultilingualString.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#prefLabel"]] if obj.get("http://www.w3.org/2004/02/skos/core#prefLabel") is not None else None,
            "http://purl.org/ontology/bibo/status": [Status.from_dict(_item) for _item in obj["http://purl.org/ontology/bibo/status"]] if obj.get("http://purl.org/ontology/bibo/status") is not None else None,
            "http://www.w3.org/2004/02/skos/core#notation": [Notation.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#notation"]] if obj.get("http://www.w3.org/2004/02/skos/core#notation") is not None else None,
            "http://www.w3.org/2004/02/skos/core#changeNote": [NonLiteralNote.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#changeNote"]] if obj.get("http://www.w3.org/2004/02/skos/core#changeNote") is not None else None,
            "http://www.w3.org/2004/02/skos/core#historyNote": [NonLiteralNote.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#historyNote"]] if obj.get("http://www.w3.org/2004/02/skos/core#historyNote") is not None else None,
            "http://www.w3.org/2004/02/skos/core#editorialNote": [NonLiteralNote.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#editorialNote"]] if obj.get("http://www.w3.org/2004/02/skos/core#editorialNote") is not None else None,
            "http://purl.org/dc/terms/created": obj.get("http://purl.org/dc/terms/created"),
            "http://purl.org/dc/terms/creator": [Node.from_dict(_item) for _item in obj["http://purl.org/dc/terms/creator"]] if obj.get("http://purl.org/dc/terms/creator") is not None else None,
            "http://www.w3.org/2002/07/owl#versionInfo": [VersionString.from_dict(_item) for _item in obj["http://www.w3.org/2002/07/owl#versionInfo"]] if obj.get("http://www.w3.org/2002/07/owl#versionInfo") is not None else None,
            "http://www.w3.org/2004/02/skos/core#definition": [MultilingualString.from_dict(_item) for _item in obj["http://www.w3.org/2004/02/skos/core#definition"]] if obj.get("http://www.w3.org/2004/02/skos/core#definition") is not None else None,
            "http://rdf-vocabulary.ddialliance.org/xkos#compares": [Node.from_dict(_item) for _item in obj["http://rdf-vocabulary.ddialliance.org/xkos#compares"]] if obj.get("http://rdf-vocabulary.ddialliance.org/xkos#compares") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


