# AssociationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://www.w3.org/TR/json-ld/#node-identifiers | 
**type** | **List[str]** | https://www.w3.org/TR/json-ld/#specifying-the-type | 
**http___rdf_vocabulary_ddialliance_org_xkossource_concept** | [**List[Node]**](Node.md) | https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences | 
**http___rdf_vocabulary_ddialliance_org_xkostarget_concept** | [**List[Node]**](Node.md) | https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences | 

## Example

```python
from pyst_client.models.association_input import AssociationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationInput from a JSON string
association_input_instance = AssociationInput.from_json(json)
# print the JSON string representation of the object
print(AssociationInput.to_json())

# convert the object into a dict
association_input_dict = association_input_instance.to_dict()
# create an instance of AssociationInput from a dict
association_input_from_dict = AssociationInput.from_dict(association_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


