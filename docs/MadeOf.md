# MadeOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://www.w3.org/TR/json-ld/#node-identifiers | 
**http___rdf_vocabulary_ddialliance_org_xkosmade_of** | [**List[Node]**](Node.md) | https://rdf-vocabulary.ddialliance.org/xkos.html#correspondences | 

## Example

```python
from pyst_client.models.made_of import MadeOf

# TODO update the JSON string below
json = "{}"
# create an instance of MadeOf from a JSON string
made_of_instance = MadeOf.from_json(json)
# print the JSON string representation of the object
print(MadeOf.to_json())

# convert the object into a dict
made_of_dict = made_of_instance.to_dict()
# create an instance of MadeOf from a dict
made_of_from_dict = MadeOf.from_dict(made_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


