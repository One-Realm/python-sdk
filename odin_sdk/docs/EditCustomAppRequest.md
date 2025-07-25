# EditCustomAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** |  | 
**project_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.edit_custom_app_request import EditCustomAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditCustomAppRequest from a JSON string
edit_custom_app_request_instance = EditCustomAppRequest.from_json(json)
# print the JSON string representation of the object
print(EditCustomAppRequest.to_json())

# convert the object into a dict
edit_custom_app_request_dict = edit_custom_app_request_instance.to_dict()
# create an instance of EditCustomAppRequest from a dict
edit_custom_app_request_from_dict = EditCustomAppRequest.from_dict(edit_custom_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


