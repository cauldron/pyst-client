# VersionString

The range for http://www.w3.org/2002/07/owl#versionInfo is http://www.w3.org/2000/01/rdf-schema#Resource, which is a class instance with no restrictions or other guidance: https://www.w3.org/TR/rdf-schema/#ch_resource.  In JSON-LD version strings would therefore be given as:  ```'http://www.w3.org/2002/07/owl#versionInfo': [{'@value': 'some_number'}]```  * It's a list because there can in theory be more than one * It uses ```{}``` syntax because it is an object, not a string  Version numbers should be numeric, so we don't need a language or text direction. However, we don't know how they are arranged, so can't convert to numeric types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 

## Example

```python
from pyst_client.models.version_string import VersionString

# TODO update the JSON string below
json = "{}"
# create an instance of VersionString from a JSON string
version_string_instance = VersionString.from_json(json)
# print the JSON string representation of the object
print(VersionString.to_json())

# convert the object into a dict
version_string_dict = version_string_instance.to_dict()
# create an instance of VersionString from a dict
version_string_from_dict = VersionString.from_dict(version_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


