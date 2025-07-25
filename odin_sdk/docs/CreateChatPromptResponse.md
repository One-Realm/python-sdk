# CreateChatPromptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**chat_id** | **str** |  | 
**metadata** | **object** |  | [optional] 
**document_keys** | **List[object]** |  | [optional] 
**document_id** | **str** |  | [optional] 
**created_at** | **float** |  | 
**custom_agent** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_chat_prompt_response import CreateChatPromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatPromptResponse from a JSON string
create_chat_prompt_response_instance = CreateChatPromptResponse.from_json(json)
# print the JSON string representation of the object
print(CreateChatPromptResponse.to_json())

# convert the object into a dict
create_chat_prompt_response_dict = create_chat_prompt_response_instance.to_dict()
# create an instance of CreateChatPromptResponse from a dict
create_chat_prompt_response_from_dict = CreateChatPromptResponse.from_dict(create_chat_prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


