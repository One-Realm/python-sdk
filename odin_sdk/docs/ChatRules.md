# ChatRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **bool** | create permission for chat | [optional] [default to False]
**view_all** | **bool** | view permission for all chats | [optional] [default to False]
**view_mine** | **bool** | view permission for my chats | [optional] [default to False]

## Example

```python
from odin_sdk.models.chat_rules import ChatRules

# TODO update the JSON string below
json = "{}"
# create an instance of ChatRules from a JSON string
chat_rules_instance = ChatRules.from_json(json)
# print the JSON string representation of the object
print(ChatRules.to_json())

# convert the object into a dict
chat_rules_dict = chat_rules_instance.to_dict()
# create an instance of ChatRules from a dict
chat_rules_from_dict = ChatRules.from_dict(chat_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


