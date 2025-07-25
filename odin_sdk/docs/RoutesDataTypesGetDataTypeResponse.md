# RoutesDataTypesGetDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**var_schema** | [**List[DTField]**](DTField.md) |  | 

## Example

```python
from odin_sdk.models.routes_data_types_get_data_type_response import RoutesDataTypesGetDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesDataTypesGetDataTypeResponse from a JSON string
routes_data_types_get_data_type_response_instance = RoutesDataTypesGetDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesDataTypesGetDataTypeResponse.to_json())

# convert the object into a dict
routes_data_types_get_data_type_response_dict = routes_data_types_get_data_type_response_instance.to_dict()
# create an instance of RoutesDataTypesGetDataTypeResponse from a dict
routes_data_types_get_data_type_response_from_dict = RoutesDataTypesGetDataTypeResponse.from_dict(routes_data_types_get_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


