# RemoveTeamMemberByEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from odin_sdk.models.remove_team_member_by_email_request import RemoveTeamMemberByEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTeamMemberByEmailRequest from a JSON string
remove_team_member_by_email_request_instance = RemoveTeamMemberByEmailRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveTeamMemberByEmailRequest.to_json())

# convert the object into a dict
remove_team_member_by_email_request_dict = remove_team_member_by_email_request_instance.to_dict()
# create an instance of RemoveTeamMemberByEmailRequest from a dict
remove_team_member_by_email_request_from_dict = RemoveTeamMemberByEmailRequest.from_dict(remove_team_member_by_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


