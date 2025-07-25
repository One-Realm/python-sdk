# UpdateDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**document_id** | **str** |  | 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**content_key** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.update_document_request import UpdateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentRequest from a JSON string
update_document_request_instance = UpdateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentRequest.to_json())

# convert the object into a dict
update_document_request_dict = update_document_request_instance.to_dict()
# create an instance of UpdateDocumentRequest from a dict
update_document_request_from_dict = UpdateDocumentRequest.from_dict(update_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


