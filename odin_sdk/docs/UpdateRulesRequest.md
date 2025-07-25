# UpdateRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**UpdateChatRules**](UpdateChatRules.md) |  | [optional] 
**assistant** | [**UpdateAssistantRules**](UpdateAssistantRules.md) |  | [optional] 
**document** | [**UpdateDocumentRules**](UpdateDocumentRules.md) |  | [optional] 
**agents** | [**UpdateAgentsRules**](UpdateAgentsRules.md) |  | [optional] 
**settings** | [**UpdateSettingsRules**](UpdateSettingsRules.md) |  | [optional] 
**add_members** | [**UpdateAddMembersRules**](UpdateAddMembersRules.md) |  | [optional] 
**kb** | [**UpdateKBRules**](UpdateKBRules.md) |  | [optional] 
**flows** | [**UpdateFlowsRules**](UpdateFlowsRules.md) |  | [optional] 
**analytics** | [**UpdateAnalyticsRules**](UpdateAnalyticsRules.md) |  | [optional] 
**actions** | [**UpdateActionsRules**](UpdateActionsRules.md) |  | [optional] 
**roles** | [**UpdateRolesRules**](UpdateRolesRules.md) |  | [optional] 

## Example

```python
from odin_sdk.models.update_rules_request import UpdateRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesRequest from a JSON string
update_rules_request_instance = UpdateRulesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRulesRequest.to_json())

# convert the object into a dict
update_rules_request_dict = update_rules_request_instance.to_dict()
# create an instance of UpdateRulesRequest from a dict
update_rules_request_from_dict = UpdateRulesRequest.from_dict(update_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


