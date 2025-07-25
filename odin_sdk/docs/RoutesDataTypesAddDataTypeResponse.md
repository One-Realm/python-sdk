# RoutesDataTypesAddDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_id** | **str** |  | 
**view_id** | **str** |  | 

## Example

```python
from odin_sdk.models.routes_data_types_add_data_type_response import RoutesDataTypesAddDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesDataTypesAddDataTypeResponse from a JSON string
routes_data_types_add_data_type_response_instance = RoutesDataTypesAddDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesDataTypesAddDataTypeResponse.to_json())

# convert the object into a dict
routes_data_types_add_data_type_response_dict = routes_data_types_add_data_type_response_instance.to_dict()
# create an instance of RoutesDataTypesAddDataTypeResponse from a dict
routes_data_types_add_data_type_response_from_dict = RoutesDataTypesAddDataTypeResponse.from_dict(routes_data_types_add_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


