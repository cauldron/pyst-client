# Concept


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://www.w3.org/TR/json-ld/#node-identifiers | 
**type** | **List[str]** | https://www.w3.org/TR/json-ld/#specifying-the-type | 
**http___www_w3_org_2004_02_skos_corepref_label** | **List[Dict[str, str]]** | https://www.w3.org/TR/skos-primer/#secpref | 
**http___purl_org_ontology_bibo_status** | **List[Dict[str, str]]** | https://github.com/dcmi/bibo/blob/main/rdf/bibo.ttl#L391 | 
**http___www_w3_org_2004_02_skos_coredefinition** | **List[Dict[str, str]]** | https://www.w3.org/TR/skos-primer/#secdocumentation | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corenotation** | **List[Dict[str, str]]** | https://www.w3.org/TR/skos-primer/#secnotations | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corechange_note** | **List[object]** |  | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corehistory_note** | **List[object]** |  | [optional] [default to []]
**http___www_w3_org_2004_02_skos_coreeditorial_note** | **List[object]** |  | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corein_scheme** | **List[object]** | https://www.w3.org/TR/skos-primer/#secscheme | 
**http___www_w3_org_2004_02_skos_corealt_label** | **List[Dict[str, str]]** | https://www.w3.org/TR/skos-primer/#secalt | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corehidden_label** | **List[Dict[str, str]]** | https://www.w3.org/TR/skos-primer/#sechidden | [optional] [default to []]
**http___www_w3_org_2004_02_skos_coretop_concept_of** | **List[object]** | https://www.w3.org/TR/skos-primer/#secscheme | [optional] [default to []]

## Example

```python
from pyst_client.models.concept import Concept

# TODO update the JSON string below
json = "{}"
# create an instance of Concept from a JSON string
concept_instance = Concept.from_json(json)
# print the JSON string representation of the object
print(Concept.to_json())

# convert the object into a dict
concept_dict = concept_instance.to_dict()
# create an instance of Concept from a dict
concept_from_dict = Concept.from_dict(concept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


