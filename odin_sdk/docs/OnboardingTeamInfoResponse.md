# OnboardingTeamInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_info** | [**OnboardingTeamInfo**](OnboardingTeamInfo.md) |  | 

## Example

```python
from odin_sdk.models.onboarding_team_info_response import OnboardingTeamInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingTeamInfoResponse from a JSON string
onboarding_team_info_response_instance = OnboardingTeamInfoResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingTeamInfoResponse.to_json())

# convert the object into a dict
onboarding_team_info_response_dict = onboarding_team_info_response_instance.to_dict()
# create an instance of OnboardingTeamInfoResponse from a dict
onboarding_team_info_response_from_dict = OnboardingTeamInfoResponse.from_dict(onboarding_team_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


