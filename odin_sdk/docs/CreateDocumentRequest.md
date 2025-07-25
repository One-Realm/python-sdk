# CreateDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**content_key** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_document_request import CreateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentRequest from a JSON string
create_document_request_instance = CreateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentRequest.to_json())

# convert the object into a dict
create_document_request_dict = create_document_request_instance.to_dict()
# create an instance of CreateDocumentRequest from a dict
create_document_request_from_dict = CreateDocumentRequest.from_dict(create_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


