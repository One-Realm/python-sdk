# RoutesProjectsGetDataTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**resource_types** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.routes_projects_get_data_types_response import RoutesProjectsGetDataTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsGetDataTypesResponse from a JSON string
routes_projects_get_data_types_response_instance = RoutesProjectsGetDataTypesResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsGetDataTypesResponse.to_json())

# convert the object into a dict
routes_projects_get_data_types_response_dict = routes_projects_get_data_types_response_instance.to_dict()
# create an instance of RoutesProjectsGetDataTypesResponse from a dict
routes_projects_get_data_types_response_from_dict = RoutesProjectsGetDataTypesResponse.from_dict(routes_projects_get_data_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


