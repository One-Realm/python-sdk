# DeployBotToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The ID of the project | 
**config** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.deploy_bot_tool_request import DeployBotToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployBotToolRequest from a JSON string
deploy_bot_tool_request_instance = DeployBotToolRequest.from_json(json)
# print the JSON string representation of the object
print(DeployBotToolRequest.to_json())

# convert the object into a dict
deploy_bot_tool_request_dict = deploy_bot_tool_request_instance.to_dict()
# create an instance of DeployBotToolRequest from a dict
deploy_bot_tool_request_from_dict = DeployBotToolRequest.from_dict(deploy_bot_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


