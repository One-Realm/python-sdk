# EditProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from odin_sdk.models.edit_project_request import EditProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectRequest from a JSON string
edit_project_request_instance = EditProjectRequest.from_json(json)
# print the JSON string representation of the object
print(EditProjectRequest.to_json())

# convert the object into a dict
edit_project_request_dict = edit_project_request_instance.to_dict()
# create an instance of EditProjectRequest from a dict
edit_project_request_from_dict = EditProjectRequest.from_dict(edit_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


