# Rules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**ChatRules**](ChatRules.md) |  | [optional] 
**assistant** | [**AssistantRules**](AssistantRules.md) |  | [optional] 
**document** | [**DocumentRules**](DocumentRules.md) |  | [optional] 
**agents** | [**AgentsRules**](AgentsRules.md) |  | [optional] 
**settings** | [**SettingsRules**](SettingsRules.md) |  | [optional] 
**add_members** | [**AddMembersRules**](AddMembersRules.md) |  | [optional] 
**kb** | [**KBRules**](KBRules.md) |  | [optional] 
**flows** | [**FlowsRules**](FlowsRules.md) |  | [optional] 
**analytics** | [**AnalyticsRules**](AnalyticsRules.md) |  | [optional] 
**actions** | [**ActionsRules**](ActionsRules.md) |  | [optional] 
**roles** | [**RolesRules**](RolesRules.md) |  | [optional] 

## Example

```python
from odin_sdk.models.rules import Rules

# TODO update the JSON string below
json = "{}"
# create an instance of Rules from a JSON string
rules_instance = Rules.from_json(json)
# print the JSON string representation of the object
print(Rules.to_json())

# convert the object into a dict
rules_dict = rules_instance.to_dict()
# create an instance of Rules from a dict
rules_from_dict = Rules.from_dict(rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


