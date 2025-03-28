# ConceptSchemeInput

Validation class for SKOS Concept Schemes.  Checks that required fields are included and have correct type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://www.w3.org/TR/json-ld/#node-identifiers | 
**type** | **List[str]** | https://www.w3.org/TR/json-ld/#specifying-the-type | 
**http___www_w3_org_2004_02_skos_corepref_label** | [**List[MultilingualString]**](MultilingualString.md) | https://www.w3.org/TR/skos-primer/#secpref | 
**http___purl_org_ontology_bibo_status** | [**List[Status]**](Status.md) | https://github.com/dcmi/bibo/blob/main/rdf/bibo.ttl#L391 | 
**http___www_w3_org_2004_02_skos_corenotation** | [**List[Notation]**](Notation.md) | https://www.w3.org/TR/skos-primer/#secnotations | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corechange_note** | [**List[NonLiteralNote]**](NonLiteralNote.md) |  | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corehistory_note** | [**List[NonLiteralNote]**](NonLiteralNote.md) |  | [optional] [default to []]
**http___www_w3_org_2004_02_skos_coreeditorial_note** | [**List[NonLiteralNote]**](NonLiteralNote.md) |  | [optional] [default to []]
**http___purl_org_dc_terms_created** | **List[datetime]** | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/created | 
**http___purl_org_dc_terms_creator** | [**List[Node]**](Node.md) | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/creator | 
**http___www_w3_org_2002_07_owlversion_info** | [**List[VersionString]**](VersionString.md) | https://www.w3.org/TR/owl-ref/#versionInfo-def | 
**http___www_w3_org_2004_02_skos_coredefinition** | [**List[MultilingualString]**](MultilingualString.md) | https://www.w3.org/TR/skos-primer/#secdocumentation | 

## Example

```python
from pyst_client.models.concept_scheme_input import ConceptSchemeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptSchemeInput from a JSON string
concept_scheme_input_instance = ConceptSchemeInput.from_json(json)
# print the JSON string representation of the object
print(ConceptSchemeInput.to_json())

# convert the object into a dict
concept_scheme_input_dict = concept_scheme_input_instance.to_dict()
# create an instance of ConceptSchemeInput from a dict
concept_scheme_input_from_dict = ConceptSchemeInput.from_dict(concept_scheme_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


