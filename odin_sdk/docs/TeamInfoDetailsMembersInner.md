# TeamInfoDetailsMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**is_pending** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.team_info_details_members_inner import TeamInfoDetailsMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfoDetailsMembersInner from a JSON string
team_info_details_members_inner_instance = TeamInfoDetailsMembersInner.from_json(json)
# print the JSON string representation of the object
print(TeamInfoDetailsMembersInner.to_json())

# convert the object into a dict
team_info_details_members_inner_dict = team_info_details_members_inner_instance.to_dict()
# create an instance of TeamInfoDetailsMembersInner from a dict
team_info_details_members_inner_from_dict = TeamInfoDetailsMembersInner.from_dict(team_info_details_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


