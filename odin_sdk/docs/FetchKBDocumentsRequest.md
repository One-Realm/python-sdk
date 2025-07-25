# FetchKBDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project id where the document is located. | 
**content_keys** | **List[str]** | The content keys to fetch - either full URLs in case of web links stored in the KB, or full filenames, e.g. &#39;example.pdf&#39;. | 

## Example

```python
from odin_sdk.models.fetch_kb_documents_request import FetchKBDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchKBDocumentsRequest from a JSON string
fetch_kb_documents_request_instance = FetchKBDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(FetchKBDocumentsRequest.to_json())

# convert the object into a dict
fetch_kb_documents_request_dict = fetch_kb_documents_request_instance.to_dict()
# create an instance of FetchKBDocumentsRequest from a dict
fetch_kb_documents_request_from_dict = FetchKBDocumentsRequest.from_dict(fetch_kb_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


