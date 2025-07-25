# OnboardingTeamInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_team** | **bool** |  | 
**team_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_size** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**member_count** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.onboarding_team_info import OnboardingTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingTeamInfo from a JSON string
onboarding_team_info_instance = OnboardingTeamInfo.from_json(json)
# print the JSON string representation of the object
print(OnboardingTeamInfo.to_json())

# convert the object into a dict
onboarding_team_info_dict = onboarding_team_info_instance.to_dict()
# create an instance of OnboardingTeamInfo from a dict
onboarding_team_info_from_dict = OnboardingTeamInfo.from_dict(onboarding_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


