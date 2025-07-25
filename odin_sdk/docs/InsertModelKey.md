# InsertModelKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** |  | 
**api_url** | **str** |  | [optional] 
**api_key** | **str** |  | 
**api_type** | **str** |  | 
**max_response_tokens** | **int** |  | 
**max_input_tokens** | **int** |  | 
**model_extra_params** | **object** |  | [optional] 
**api_version** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.insert_model_key import InsertModelKey

# TODO update the JSON string below
json = "{}"
# create an instance of InsertModelKey from a JSON string
insert_model_key_instance = InsertModelKey.from_json(json)
# print the JSON string representation of the object
print(InsertModelKey.to_json())

# convert the object into a dict
insert_model_key_dict = insert_model_key_instance.to_dict()
# create an instance of InsertModelKey from a dict
insert_model_key_from_dict = InsertModelKey.from_dict(insert_model_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


