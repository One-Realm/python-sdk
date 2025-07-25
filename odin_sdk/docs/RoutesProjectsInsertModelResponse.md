# RoutesProjectsInsertModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.routes_projects_insert_model_response import RoutesProjectsInsertModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsInsertModelResponse from a JSON string
routes_projects_insert_model_response_instance = RoutesProjectsInsertModelResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsInsertModelResponse.to_json())

# convert the object into a dict
routes_projects_insert_model_response_dict = routes_projects_insert_model_response_instance.to_dict()
# create an instance of RoutesProjectsInsertModelResponse from a dict
routes_projects_insert_model_response_from_dict = RoutesProjectsInsertModelResponse.from_dict(routes_projects_insert_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


