# UpdateDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**document** | [**Document**](Document.md) |  | 

## Example

```python
from odin_sdk.models.update_document_response import UpdateDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentResponse from a JSON string
update_document_response_instance = UpdateDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentResponse.to_json())

# convert the object into a dict
update_document_response_dict = update_document_response_instance.to_dict()
# create an instance of UpdateDocumentResponse from a dict
update_document_response_from_dict = UpdateDocumentResponse.from_dict(update_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


