# FetchAllUserLevelIntegrationsForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[UserLevelIntegration]**](UserLevelIntegration.md) |  | 

## Example

```python
from odin_sdk.models.fetch_all_user_level_integrations_for_user_response import FetchAllUserLevelIntegrationsForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAllUserLevelIntegrationsForUserResponse from a JSON string
fetch_all_user_level_integrations_for_user_response_instance = FetchAllUserLevelIntegrationsForUserResponse.from_json(json)
# print the JSON string representation of the object
print(FetchAllUserLevelIntegrationsForUserResponse.to_json())

# convert the object into a dict
fetch_all_user_level_integrations_for_user_response_dict = fetch_all_user_level_integrations_for_user_response_instance.to_dict()
# create an instance of FetchAllUserLevelIntegrationsForUserResponse from a dict
fetch_all_user_level_integrations_for_user_response_from_dict = FetchAllUserLevelIntegrationsForUserResponse.from_dict(fetch_all_user_level_integrations_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


