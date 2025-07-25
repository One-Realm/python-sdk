# GetProjectMembersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ProjectMember]**](ProjectMember.md) |  | 

## Example

```python
from odin_sdk.models.get_project_members_response import GetProjectMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectMembersResponse from a JSON string
get_project_members_response_instance = GetProjectMembersResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectMembersResponse.to_json())

# convert the object into a dict
get_project_members_response_dict = get_project_members_response_instance.to_dict()
# create an instance of GetProjectMembersResponse from a dict
get_project_members_response_from_dict = GetProjectMembersResponse.from_dict(get_project_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


