# GenerateSuggestionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Message]**](Message.md) |  | 
**no_of_suggestions** | **int** |  | 
**conversation_type** | **str** |  | 
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**model_name** | **str** |  | [optional] [default to 'gpt-4o-mini']
**system_prompt** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from odin_sdk.models.generate_suggestions_request import GenerateSuggestionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSuggestionsRequest from a JSON string
generate_suggestions_request_instance = GenerateSuggestionsRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateSuggestionsRequest.to_json())

# convert the object into a dict
generate_suggestions_request_dict = generate_suggestions_request_instance.to_dict()
# create an instance of GenerateSuggestionsRequest from a dict
generate_suggestions_request_from_dict = GenerateSuggestionsRequest.from_dict(generate_suggestions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


