# MultilingualString

A dictionary which provides a language-tagged string literal compatible with JSON-LD 1.1.  The language code must be compliant with BCP 47: https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string  We use the `langcodes` library to ensure this compliance, and to fix common errors: https://pypi.org/project/langcodes/  The direction is not required by the JSON-LD standard, but we will always include it to make code more predictable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**language** | **str** |  | 
**direction** | **str** |  | [optional] [default to 'ltr']

## Example

```python
from pyst_client.models.multilingual_string import MultilingualString

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualString from a JSON string
multilingual_string_instance = MultilingualString.from_json(json)
# print the JSON string representation of the object
print(MultilingualString.to_json())

# convert the object into a dict
multilingual_string_dict = multilingual_string_instance.to_dict()
# create an instance of MultilingualString from a dict
multilingual_string_from_dict = MultilingualString.from_dict(multilingual_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


