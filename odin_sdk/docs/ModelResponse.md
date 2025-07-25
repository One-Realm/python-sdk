# ModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** |  | 
**api_url** | **str** |  | 
**api_type** | **str** |  | 
**max_input_tokens** | **int** |  | 
**max_response_tokens** | **int** |  | 
**display_name** | **str** |  | 
**cost** | **int** |  | 
**hidden** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_default_extraction_model** | **bool** |  | [optional] 
**is_default_citation_model** | **bool** |  | [optional] 
**model_extra_params** | [**ModelExtraParams**](ModelExtraParams.md) |  | [optional] 
**model_id** | **str** |  | 

## Example

```python
from odin_sdk.models.model_response import ModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelResponse from a JSON string
model_response_instance = ModelResponse.from_json(json)
# print the JSON string representation of the object
print(ModelResponse.to_json())

# convert the object into a dict
model_response_dict = model_response_instance.to_dict()
# create an instance of ModelResponse from a dict
model_response_from_dict = ModelResponse.from_dict(model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


