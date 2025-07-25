# AddUserToProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**users** | [**List[UserDetails]**](UserDetails.md) |  | 
**send_mail** | **bool** |  | [optional] [default to True]

## Example

```python
from odin_sdk.models.add_user_to_project_request import AddUserToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToProjectRequest from a JSON string
add_user_to_project_request_instance = AddUserToProjectRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserToProjectRequest.to_json())

# convert the object into a dict
add_user_to_project_request_dict = add_user_to_project_request_instance.to_dict()
# create an instance of AddUserToProjectRequest from a dict
add_user_to_project_request_from_dict = AddUserToProjectRequest.from_dict(add_user_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


