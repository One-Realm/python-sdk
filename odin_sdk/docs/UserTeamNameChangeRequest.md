# UserTeamNameChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** |  | 

## Example

```python
from odin_sdk.models.user_team_name_change_request import UserTeamNameChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamNameChangeRequest from a JSON string
user_team_name_change_request_instance = UserTeamNameChangeRequest.from_json(json)
# print the JSON string representation of the object
print(UserTeamNameChangeRequest.to_json())

# convert the object into a dict
user_team_name_change_request_dict = user_team_name_change_request_instance.to_dict()
# create an instance of UserTeamNameChangeRequest from a dict
user_team_name_change_request_from_dict = UserTeamNameChangeRequest.from_dict(user_team_name_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


