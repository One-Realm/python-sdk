# GetDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**document_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_document_request import GetDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentRequest from a JSON string
get_document_request_instance = GetDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentRequest.to_json())

# convert the object into a dict
get_document_request_dict = get_document_request_instance.to_dict()
# create an instance of GetDocumentRequest from a dict
get_document_request_from_dict = GetDocumentRequest.from_dict(get_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


