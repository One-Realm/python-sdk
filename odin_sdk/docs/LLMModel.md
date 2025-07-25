# LLMModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The unique key for the model, for example azure-gpt4. | 
**display_name** | **str** | The name of the model to display in the UI. | 
**name** | **str** | The name of the model. | 
**api_type** | **str** | The type of the API, for example openai. | 
**cost** | **float** | The cost of the model, in credits. | 
**free_plan** | **bool** | Whether the model is available on the free plan. | 
**hidden** | **bool** | Whether the model is hidden from the UI. | 

## Example

```python
from odin_sdk.models.llm_model import LLMModel

# TODO update the JSON string below
json = "{}"
# create an instance of LLMModel from a JSON string
llm_model_instance = LLMModel.from_json(json)
# print the JSON string representation of the object
print(LLMModel.to_json())

# convert the object into a dict
llm_model_dict = llm_model_instance.to_dict()
# create an instance of LLMModel from a dict
llm_model_from_dict = LLMModel.from_dict(llm_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


