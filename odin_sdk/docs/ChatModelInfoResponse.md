# ChatModelInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_models** | [**List[LLMModel]**](LLMModel.md) | The available chat models | 

## Example

```python
from odin_sdk.models.chat_model_info_response import ChatModelInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatModelInfoResponse from a JSON string
chat_model_info_response_instance = ChatModelInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ChatModelInfoResponse.to_json())

# convert the object into a dict
chat_model_info_response_dict = chat_model_info_response_instance.to_dict()
# create an instance of ChatModelInfoResponse from a dict
chat_model_info_response_from_dict = ChatModelInfoResponse.from_dict(chat_model_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


