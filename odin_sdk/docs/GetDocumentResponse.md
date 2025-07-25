# GetDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**document** | [**Document**](Document.md) |  | 

## Example

```python
from odin_sdk.models.get_document_response import GetDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentResponse from a JSON string
get_document_response_instance = GetDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentResponse.to_json())

# convert the object into a dict
get_document_response_dict = get_document_response_instance.to_dict()
# create an instance of GetDocumentResponse from a dict
get_document_response_from_dict = GetDocumentResponse.from_dict(get_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


