# JiraLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri_from_callback** | **str** |  | 

## Example

```python
from odin_sdk.models.jira_login_request import JiraLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JiraLoginRequest from a JSON string
jira_login_request_instance = JiraLoginRequest.from_json(json)
# print the JSON string representation of the object
print(JiraLoginRequest.to_json())

# convert the object into a dict
jira_login_request_dict = jira_login_request_instance.to_dict()
# create an instance of JiraLoginRequest from a dict
jira_login_request_from_dict = JiraLoginRequest.from_dict(jira_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


