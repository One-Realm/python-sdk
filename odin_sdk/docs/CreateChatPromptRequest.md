# CreateChatPromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**name** | **str** |  | [optional] 
**context** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**document_keys** | **List[object]** |  | [optional] 
**document_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_chat_prompt_request import CreateChatPromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatPromptRequest from a JSON string
create_chat_prompt_request_instance = CreateChatPromptRequest.from_json(json)
# print the JSON string representation of the object
print(CreateChatPromptRequest.to_json())

# convert the object into a dict
create_chat_prompt_request_dict = create_chat_prompt_request_instance.to_dict()
# create an instance of CreateChatPromptRequest from a dict
create_chat_prompt_request_from_dict = CreateChatPromptRequest.from_dict(create_chat_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


