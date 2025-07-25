# DeployBotToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the bot deployment was successful | 
**message** | **str** | A message describing the result | 
**response** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.deploy_bot_tool_response import DeployBotToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployBotToolResponse from a JSON string
deploy_bot_tool_response_instance = DeployBotToolResponse.from_json(json)
# print the JSON string representation of the object
print(DeployBotToolResponse.to_json())

# convert the object into a dict
deploy_bot_tool_response_dict = deploy_bot_tool_response_instance.to_dict()
# create an instance of DeployBotToolResponse from a dict
deploy_bot_tool_response_from_dict = DeployBotToolResponse.from_dict(deploy_bot_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


