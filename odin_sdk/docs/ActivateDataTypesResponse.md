# ActivateDataTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_id** | **str** |  | 

## Example

```python
from odin_sdk.models.activate_data_types_response import ActivateDataTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateDataTypesResponse from a JSON string
activate_data_types_response_instance = ActivateDataTypesResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateDataTypesResponse.to_json())

# convert the object into a dict
activate_data_types_response_dict = activate_data_types_response_instance.to_dict()
# create an instance of ActivateDataTypesResponse from a dict
activate_data_types_response_from_dict = ActivateDataTypesResponse.from_dict(activate_data_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


