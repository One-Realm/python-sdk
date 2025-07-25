# CreateDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**document** | [**Document**](Document.md) |  | 

## Example

```python
from odin_sdk.models.create_document_response import CreateDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentResponse from a JSON string
create_document_response_instance = CreateDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentResponse.to_json())

# convert the object into a dict
create_document_response_dict = create_document_response_instance.to_dict()
# create an instance of CreateDocumentResponse from a dict
create_document_response_from_dict = CreateDocumentResponse.from_dict(create_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


