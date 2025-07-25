# ModelCreate


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
from odin_sdk.models.model_create import ModelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCreate from a JSON string
model_create_instance = ModelCreate.from_json(json)
# print the JSON string representation of the object
print(ModelCreate.to_json())

# convert the object into a dict
model_create_dict = model_create_instance.to_dict()
# create an instance of ModelCreate from a dict
model_create_from_dict = ModelCreate.from_dict(model_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


