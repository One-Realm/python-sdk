# CustomChatbot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_placeholder_text** | **str** |  | [optional] 
**display_sources** | **bool** |  | [optional] 
**primary_color** | **str** |  | [optional] 
**font_size** | **str** |  | [optional] 
**toggle_icon_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**caret_bg_color** | **str** |  | [optional] 
**suggestions** | **List[str]** |  | [optional] 
**chatbot_name** | **str** |  | [optional] 
**enable_multiple_chats** | **bool** |  | [optional] 
**auto_show_welcome_message_after** | **str** |  | [optional] 
**welcome_message** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.custom_chatbot import CustomChatbot

# TODO update the JSON string below
json = "{}"
# create an instance of CustomChatbot from a JSON string
custom_chatbot_instance = CustomChatbot.from_json(json)
# print the JSON string representation of the object
print(CustomChatbot.to_json())

# convert the object into a dict
custom_chatbot_dict = custom_chatbot_instance.to_dict()
# create an instance of CustomChatbot from a dict
custom_chatbot_from_dict = CustomChatbot.from_dict(custom_chatbot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


