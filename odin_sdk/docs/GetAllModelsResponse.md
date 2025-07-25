# GetAllModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[GetModelResponse]**](GetModelResponse.md) |  | 

## Example

```python
from odin_sdk.models.get_all_models_response import GetAllModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllModelsResponse from a JSON string
get_all_models_response_instance = GetAllModelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllModelsResponse.to_json())

# convert the object into a dict
get_all_models_response_dict = get_all_models_response_instance.to_dict()
# create an instance of GetAllModelsResponse from a dict
get_all_models_response_from_dict = GetAllModelsResponse.from_dict(get_all_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


