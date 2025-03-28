# RelationshipOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://www.w3.org/TR/json-ld/#node-identifiers | 
**http___www_w3_org_2004_02_skos_corebroader** | **List[object]** | https://www.w3.org/TR/skos-primer/#sechierarchy | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corenarrower** | **List[object]** | https://www.w3.org/TR/skos-primer/#sechierarchy | [optional] [default to []]
**http___www_w3_org_2004_02_skos_coreexact_match** | **List[object]** | https://www.w3.org/TR/skos-primer/#secassociative | [optional] [default to []]
**http___www_w3_org_2004_02_skos_coreclose_match** | **List[object]** | https://www.w3.org/TR/skos-primer/#secassociative | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corebroad_match** | **List[object]** | https://www.w3.org/TR/skos-primer/#secassociative | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corenarrow_match** | **List[object]** | https://www.w3.org/TR/skos-primer/#secassociative | [optional] [default to []]
**http___www_w3_org_2004_02_skos_corerelated_match** | **List[object]** | https://www.w3.org/TR/skos-primer/#secassociative | [optional] [default to []]

## Example

```python
from pyst_client.models.relationship_output import RelationshipOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipOutput from a JSON string
relationship_output_instance = RelationshipOutput.from_json(json)
# print the JSON string representation of the object
print(RelationshipOutput.to_json())

# convert the object into a dict
relationship_output_dict = relationship_output_instance.to_dict()
# create an instance of RelationshipOutput from a dict
relationship_output_from_dict = RelationshipOutput.from_dict(relationship_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


