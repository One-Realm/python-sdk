# TeamMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from odin_sdk.models.team_members_request import TeamMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMembersRequest from a JSON string
team_members_request_instance = TeamMembersRequest.from_json(json)
# print the JSON string representation of the object
print(TeamMembersRequest.to_json())

# convert the object into a dict
team_members_request_dict = team_members_request_instance.to_dict()
# create an instance of TeamMembersRequest from a dict
team_members_request_from_dict = TeamMembersRequest.from_dict(team_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


