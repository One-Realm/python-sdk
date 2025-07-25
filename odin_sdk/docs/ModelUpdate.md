# ModelUpdate


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

## Example

```python
from odin_sdk.models.model_update import ModelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUpdate from a JSON string
model_update_instance = ModelUpdate.from_json(json)
# print the JSON string representation of the object
print(ModelUpdate.to_json())

# convert the object into a dict
model_update_dict = model_update_instance.to_dict()
# create an instance of ModelUpdate from a dict
model_update_from_dict = ModelUpdate.from_dict(model_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


