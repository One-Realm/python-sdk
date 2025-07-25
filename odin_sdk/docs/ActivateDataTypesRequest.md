# ActivateDataTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **str** |  | 

## Example

```python
from odin_sdk.models.activate_data_types_request import ActivateDataTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateDataTypesRequest from a JSON string
activate_data_types_request_instance = ActivateDataTypesRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateDataTypesRequest.to_json())

# convert the object into a dict
activate_data_types_request_dict = activate_data_types_request_instance.to_dict()
# create an instance of ActivateDataTypesRequest from a dict
activate_data_types_request_from_dict = ActivateDataTypesRequest.from_dict(activate_data_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


