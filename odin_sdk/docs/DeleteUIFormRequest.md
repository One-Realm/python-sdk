# DeleteUIFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**message_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.delete_ui_form_request import DeleteUIFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUIFormRequest from a JSON string
delete_ui_form_request_instance = DeleteUIFormRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteUIFormRequest.to_json())

# convert the object into a dict
delete_ui_form_request_dict = delete_ui_form_request_instance.to_dict()
# create an instance of DeleteUIFormRequest from a dict
delete_ui_form_request_from_dict = DeleteUIFormRequest.from_dict(delete_ui_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


