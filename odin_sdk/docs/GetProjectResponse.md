# GetProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_data** | **object** |  | 
**test_groups** | **List[object]** |  | 
**role** | [**GetRoleResponse**](GetRoleResponse.md) |  | 

## Example

```python
from odin_sdk.models.get_project_response import GetProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectResponse from a JSON string
get_project_response_instance = GetProjectResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectResponse.to_json())

# convert the object into a dict
get_project_response_dict = get_project_response_instance.to_dict()
# create an instance of GetProjectResponse from a dict
get_project_response_from_dict = GetProjectResponse.from_dict(get_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


