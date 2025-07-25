# SearchKBDocumentsByNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[ResponseSearchDocumentData]**](ResponseSearchDocumentData.md) | The list of document metadata fetched from the KB. | 

## Example

```python
from odin_sdk.models.search_kb_documents_by_name_response import SearchKBDocumentsByNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchKBDocumentsByNameResponse from a JSON string
search_kb_documents_by_name_response_instance = SearchKBDocumentsByNameResponse.from_json(json)
# print the JSON string representation of the object
print(SearchKBDocumentsByNameResponse.to_json())

# convert the object into a dict
search_kb_documents_by_name_response_dict = search_kb_documents_by_name_response_instance.to_dict()
# create an instance of SearchKBDocumentsByNameResponse from a dict
search_kb_documents_by_name_response_from_dict = SearchKBDocumentsByNameResponse.from_dict(search_kb_documents_by_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


