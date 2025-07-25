# UpdateChatRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_all** | **bool** |  | [optional] 
**view_mine** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_chat_rules import UpdateChatRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatRules from a JSON string
update_chat_rules_instance = UpdateChatRules.from_json(json)
# print the JSON string representation of the object
print(UpdateChatRules.to_json())

# convert the object into a dict
update_chat_rules_dict = update_chat_rules_instance.to_dict()
# create an instance of UpdateChatRules from a dict
update_chat_rules_from_dict = UpdateChatRules.from_dict(update_chat_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


