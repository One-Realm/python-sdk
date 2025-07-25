# FetchKBDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[RoutesToolsResponseKBDocument]**](RoutesToolsResponseKBDocument.md) | The list of documents fetched from the KB. | 

## Example

```python
from odin_sdk.models.fetch_kb_documents_response import FetchKBDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchKBDocumentsResponse from a JSON string
fetch_kb_documents_response_instance = FetchKBDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(FetchKBDocumentsResponse.to_json())

# convert the object into a dict
fetch_kb_documents_response_dict = fetch_kb_documents_response_instance.to_dict()
# create an instance of FetchKBDocumentsResponse from a dict
fetch_kb_documents_response_from_dict = FetchKBDocumentsResponse.from_dict(fetch_kb_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


