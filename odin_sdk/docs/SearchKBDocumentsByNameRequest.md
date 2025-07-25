# SearchKBDocumentsByNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_keys** | **List[str]** | The search keys to fetch - full or partial filenames and urls, or just keywords. | 

## Example

```python
from odin_sdk.models.search_kb_documents_by_name_request import SearchKBDocumentsByNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchKBDocumentsByNameRequest from a JSON string
search_kb_documents_by_name_request_instance = SearchKBDocumentsByNameRequest.from_json(json)
# print the JSON string representation of the object
print(SearchKBDocumentsByNameRequest.to_json())

# convert the object into a dict
search_kb_documents_by_name_request_dict = search_kb_documents_by_name_request_instance.to_dict()
# create an instance of SearchKBDocumentsByNameRequest from a dict
search_kb_documents_by_name_request_from_dict = SearchKBDocumentsByNameRequest.from_dict(search_kb_documents_by_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


