# RoutesProjectsAddDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**resource_type_id** | **str** |  | 

## Example

```python
from odin_sdk.models.routes_projects_add_data_type_response import RoutesProjectsAddDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsAddDataTypeResponse from a JSON string
routes_projects_add_data_type_response_instance = RoutesProjectsAddDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsAddDataTypeResponse.to_json())

# convert the object into a dict
routes_projects_add_data_type_response_dict = routes_projects_add_data_type_response_instance.to_dict()
# create an instance of RoutesProjectsAddDataTypeResponse from a dict
routes_projects_add_data_type_response_from_dict = RoutesProjectsAddDataTypeResponse.from_dict(routes_projects_add_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


