# GetChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**metadata** | **object** |  | [optional] 
**created_at** | **float** |  | [optional] 
**messages** | **List[object]** |  | [optional] 
**name** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**document_keys** | **List[object]** |  | [optional] 
**custom_agent** | **str** |  | [optional] 
**chat_files_metadata** | **List[object]** |  | [optional] 
**debug_prompt_info** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.get_chat_response import GetChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatResponse from a JSON string
get_chat_response_instance = GetChatResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatResponse.to_json())

# convert the object into a dict
get_chat_response_dict = get_chat_response_instance.to_dict()
# create an instance of GetChatResponse from a dict
get_chat_response_from_dict = GetChatResponse.from_dict(get_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


