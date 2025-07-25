# RoutesProjectsAddDataTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type_id** | **str** |  | [optional] 
**title** | **str** | The title of the resource type. | 
**description** | **str** | A brief description of the resource type. | 
**metadata** | [**List[DataTypesMetadataField]**](DataTypesMetadataField.md) | A list of metadata fields for the resource type. | 

## Example

```python
from odin_sdk.models.routes_projects_add_data_type_request import RoutesProjectsAddDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsAddDataTypeRequest from a JSON string
routes_projects_add_data_type_request_instance = RoutesProjectsAddDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsAddDataTypeRequest.to_json())

# convert the object into a dict
routes_projects_add_data_type_request_dict = routes_projects_add_data_type_request_instance.to_dict()
# create an instance of RoutesProjectsAddDataTypeRequest from a dict
routes_projects_add_data_type_request_from_dict = RoutesProjectsAddDataTypeRequest.from_dict(routes_projects_add_data_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


