# TeamMemberModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**is_pending** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.team_member_model import TeamMemberModel

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberModel from a JSON string
team_member_model_instance = TeamMemberModel.from_json(json)
# print the JSON string representation of the object
print(TeamMemberModel.to_json())

# convert the object into a dict
team_member_model_dict = team_member_model_instance.to_dict()
# create an instance of TeamMemberModel from a dict
team_member_model_from_dict = TeamMemberModel.from_dict(team_member_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


