# CorrespondenceOutput


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
**http___purl_org_dc_terms_created** | **List[object]** | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/created | 
**http___purl_org_dc_terms_creator** | **List[object]** | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/creator | 
**http___www_w3_org_2002_07_owlversion_info** | **List[object]** | https://www.w3.org/TR/owl-ref/#versionInfo-def | 
**http___rdf_vocabulary_ddialliance_org_xkoscompares** | **List[object]** | https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences | 
**http___rdf_vocabulary_ddialliance_org_xkosmade_of** | **List[object]** | https://www.w3.org/TR/skos-primer/#secdocumentation | [optional] [default to []]

## Example

```python
from pyst_client.models.correspondence_output import CorrespondenceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CorrespondenceOutput from a JSON string
correspondence_output_instance = CorrespondenceOutput.from_json(json)
# print the JSON string representation of the object
print(CorrespondenceOutput.to_json())

# convert the object into a dict
correspondence_output_dict = correspondence_output_instance.to_dict()
# create an instance of CorrespondenceOutput from a dict
correspondence_output_from_dict = CorrespondenceOutput.from_dict(correspondence_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


