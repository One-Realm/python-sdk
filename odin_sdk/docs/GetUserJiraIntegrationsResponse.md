# GetUserJiraIntegrationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[JiraIntegration]**](JiraIntegration.md) |  | 

## Example

```python
from odin_sdk.models.get_user_jira_integrations_response import GetUserJiraIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserJiraIntegrationsResponse from a JSON string
get_user_jira_integrations_response_instance = GetUserJiraIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserJiraIntegrationsResponse.to_json())

# convert the object into a dict
get_user_jira_integrations_response_dict = get_user_jira_integrations_response_instance.to_dict()
# create an instance of GetUserJiraIntegrationsResponse from a dict
get_user_jira_integrations_response_from_dict = GetUserJiraIntegrationsResponse.from_dict(get_user_jira_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


