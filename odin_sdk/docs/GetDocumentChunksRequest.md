# GetDocumentChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_key** | **str** | The document key to fetch chunks for - either full URL for web links or filename for uploaded files | 
**page** | **int** | Page number to fetch (starts at 1) | [optional] [default to 1]
**page_size** | **int** | Number of chunks per page | [optional] [default to 10]

## Example

```python
from odin_sdk.models.get_document_chunks_request import GetDocumentChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentChunksRequest from a JSON string
get_document_chunks_request_instance = GetDocumentChunksRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentChunksRequest.to_json())

# convert the object into a dict
get_document_chunks_request_dict = get_document_chunks_request_instance.to_dict()
# create an instance of GetDocumentChunksRequest from a dict
get_document_chunks_request_from_dict = GetDocumentChunksRequest.from_dict(get_document_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


