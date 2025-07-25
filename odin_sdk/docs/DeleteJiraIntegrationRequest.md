# DeleteJiraIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_jira_integration_request import DeleteJiraIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteJiraIntegrationRequest from a JSON string
delete_jira_integration_request_instance = DeleteJiraIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteJiraIntegrationRequest.to_json())

# convert the object into a dict
delete_jira_integration_request_dict = delete_jira_integration_request_instance.to_dict()
# create an instance of DeleteJiraIntegrationRequest from a dict
delete_jira_integration_request_from_dict = DeleteJiraIntegrationRequest.from_dict(delete_jira_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


