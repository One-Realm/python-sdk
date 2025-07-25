# RoutesDataTypesGetDataTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_types** | [**List[DataTypeWithSchema]**](DataTypeWithSchema.md) |  | 

## Example

```python
from odin_sdk.models.routes_data_types_get_data_types_response import RoutesDataTypesGetDataTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesDataTypesGetDataTypesResponse from a JSON string
routes_data_types_get_data_types_response_instance = RoutesDataTypesGetDataTypesResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesDataTypesGetDataTypesResponse.to_json())

# convert the object into a dict
routes_data_types_get_data_types_response_dict = routes_data_types_get_data_types_response_instance.to_dict()
# create an instance of RoutesDataTypesGetDataTypesResponse from a dict
routes_data_types_get_data_types_response_from_dict = RoutesDataTypesGetDataTypesResponse.from_dict(routes_data_types_get_data_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


