# GetAllRoleNamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[Role]**](Role.md) |  | 

## Example

```python
from odin_sdk.models.get_all_role_names_response import GetAllRoleNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllRoleNamesResponse from a JSON string
get_all_role_names_response_instance = GetAllRoleNamesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllRoleNamesResponse.to_json())

# convert the object into a dict
get_all_role_names_response_dict = get_all_role_names_response_instance.to_dict()
# create an instance of GetAllRoleNamesResponse from a dict
get_all_role_names_response_from_dict = GetAllRoleNamesResponse.from_dict(get_all_role_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


