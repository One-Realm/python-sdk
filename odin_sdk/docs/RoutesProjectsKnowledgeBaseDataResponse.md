# RoutesProjectsKnowledgeBaseDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**content** | **str** |  | 
**document_data** | **object** |  | 
**url** | **str** |  | [optional] 
**uploaded_by** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**document_key** | **str** |  | 
**data_type_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_knowledge_base_data_response import RoutesProjectsKnowledgeBaseDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsKnowledgeBaseDataResponse from a JSON string
routes_projects_knowledge_base_data_response_instance = RoutesProjectsKnowledgeBaseDataResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsKnowledgeBaseDataResponse.to_json())

# convert the object into a dict
routes_projects_knowledge_base_data_response_dict = routes_projects_knowledge_base_data_response_instance.to_dict()
# create an instance of RoutesProjectsKnowledgeBaseDataResponse from a dict
routes_projects_knowledge_base_data_response_from_dict = RoutesProjectsKnowledgeBaseDataResponse.from_dict(routes_projects_knowledge_base_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


