# JiraIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**jira_email** | **str** |  | 

## Example

```python
from odin_sdk.models.jira_integration import JiraIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of JiraIntegration from a JSON string
jira_integration_instance = JiraIntegration.from_json(json)
# print the JSON string representation of the object
print(JiraIntegration.to_json())

# convert the object into a dict
jira_integration_dict = jira_integration_instance.to_dict()
# create an instance of JiraIntegration from a dict
jira_integration_from_dict = JiraIntegration.from_dict(jira_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


