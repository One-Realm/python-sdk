# AddUserToProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**users** | [**List[UserInfo]**](UserInfo.md) |  | [optional] 

## Example

```python
from odin_sdk.models.add_user_to_project_response import AddUserToProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToProjectResponse from a JSON string
add_user_to_project_response_instance = AddUserToProjectResponse.from_json(json)
# print the JSON string representation of the object
print(AddUserToProjectResponse.to_json())

# convert the object into a dict
add_user_to_project_response_dict = add_user_to_project_response_instance.to_dict()
# create an instance of AddUserToProjectResponse from a dict
add_user_to_project_response_from_dict = AddUserToProjectResponse.from_dict(add_user_to_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


