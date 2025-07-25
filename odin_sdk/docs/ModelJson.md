# ModelJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.model_json import ModelJson

# TODO update the JSON string below
json = "{}"
# create an instance of ModelJson from a JSON string
model_json_instance = ModelJson.from_json(json)
# print the JSON string representation of the object
print(ModelJson.to_json())

# convert the object into a dict
model_json_dict = model_json_instance.to_dict()
# create an instance of ModelJson from a dict
model_json_from_dict = ModelJson.from_dict(model_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


