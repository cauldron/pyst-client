# NonLiteralNote

Used for skos:changeNote, skos:historyNote, and skos:editorialNote.  SKOS allows for string literals but we require an author and timestamp for each.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http___www_w3_org_1999_02_22_rdf_syntax_nsvalue** | [**List[MultilingualString]**](MultilingualString.md) |  | 
**http___purl_org_dc_terms_creator** | [**List[Node]**](Node.md) |  | 
**http___purl_org_dc_terms_issued** | **List[datetime]** |  | 

## Example

```python
from pyst_client.models.non_literal_note import NonLiteralNote

# TODO update the JSON string below
json = "{}"
# create an instance of NonLiteralNote from a JSON string
non_literal_note_instance = NonLiteralNote.from_json(json)
# print the JSON string representation of the object
print(NonLiteralNote.to_json())

# convert the object into a dict
non_literal_note_dict = non_literal_note_instance.to_dict()
# create an instance of NonLiteralNote from a dict
non_literal_note_from_dict = NonLiteralNote.from_dict(non_literal_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


