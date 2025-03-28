# DateTime

The range for http://purl.org/dc/terms/created is http://www.w3.org/2000/01/rdf-schema#Literal. We will be more strict and require an ISO 8601 date or datetime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DateTimeType**](DateTimeType.md) |  | 
**value** | **datetime** |  | 

## Example

```python
from pyst_client.models.date_time import DateTime

# TODO update the JSON string below
json = "{}"
# create an instance of DateTime from a JSON string
date_time_instance = DateTime.from_json(json)
# print the JSON string representation of the object
print(DateTime.to_json())

# convert the object into a dict
date_time_dict = date_time_instance.to_dict()
# create an instance of DateTime from a dict
date_time_from_dict = DateTime.from_dict(date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


