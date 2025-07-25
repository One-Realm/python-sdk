# UpdateUserOnboardingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_size** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**goal** | **str** |  | [optional] 
**work_apps** | **List[str]** |  | [optional] 
**onboarding_completed** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_user_onboarding_request import UpdateUserOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserOnboardingRequest from a JSON string
update_user_onboarding_request_instance = UpdateUserOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserOnboardingRequest.to_json())

# convert the object into a dict
update_user_onboarding_request_dict = update_user_onboarding_request_instance.to_dict()
# create an instance of UpdateUserOnboardingRequest from a dict
update_user_onboarding_request_from_dict = UpdateUserOnboardingRequest.from_dict(update_user_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


