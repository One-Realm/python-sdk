# UpdateTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** |  | 
**team_members** | [**List[TeamMembersRequest]**](TeamMembersRequest.md) |  | 

## Example

```python
from odin_sdk.models.update_team_request import UpdateTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamRequest from a JSON string
update_team_request_instance = UpdateTeamRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamRequest.to_json())

# convert the object into a dict
update_team_request_dict = update_team_request_instance.to_dict()
# create an instance of UpdateTeamRequest from a dict
update_team_request_from_dict = UpdateTeamRequest.from_dict(update_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


