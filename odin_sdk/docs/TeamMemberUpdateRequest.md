# TeamMemberUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from odin_sdk.models.team_member_update_request import TeamMemberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberUpdateRequest from a JSON string
team_member_update_request_instance = TeamMemberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TeamMemberUpdateRequest.to_json())

# convert the object into a dict
team_member_update_request_dict = team_member_update_request_instance.to_dict()
# create an instance of TeamMemberUpdateRequest from a dict
team_member_update_request_from_dict = TeamMemberUpdateRequest.from_dict(team_member_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


