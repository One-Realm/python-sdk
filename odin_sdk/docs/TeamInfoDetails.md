# TeamInfoDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**admin** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**credits** | **int** |  | [optional] 
**used_credits** | **int** |  | [optional] 
**bonus_credits** | **int** |  | [optional] 
**allowed_seats** | **int** |  | [optional] 
**team_id** | **str** |  | [optional] 
**members** | [**List[TeamInfoDetailsMembersInner]**](TeamInfoDetailsMembersInner.md) |  | [optional] 
**email_domain** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**plan_type** | **str** |  | [optional] 
**api_keys** | [**Dict[str, TeamInfoDetailsApiKeysValue]**](TeamInfoDetailsApiKeysValue.md) |  | [optional] 
**settings** | **object** |  | [optional] 
**aihub_projects_whitelist** | **List[str]** |  | [optional] 

## Example

```python
from odin_sdk.models.team_info_details import TeamInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfoDetails from a JSON string
team_info_details_instance = TeamInfoDetails.from_json(json)
# print the JSON string representation of the object
print(TeamInfoDetails.to_json())

# convert the object into a dict
team_info_details_dict = team_info_details_instance.to_dict()
# create an instance of TeamInfoDetails from a dict
team_info_details_from_dict = TeamInfoDetails.from_dict(team_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


