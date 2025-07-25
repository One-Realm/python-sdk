# RoutesKnowledgebaseKnowledgeBaseDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**content** | **str** |  | 
**document_data** | **object** |  | 
**url** | **str** |  | [optional] 
**uploaded_by** | **str** |  | [optional] 
**status** | [**KBFileStatus**](KBFileStatus.md) |  | [optional] 
**size** | **int** |  | [optional] 
**document_key** | **str** |  | 
**data_type_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.routes_knowledgebase_knowledge_base_data_response import RoutesKnowledgebaseKnowledgeBaseDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesKnowledgebaseKnowledgeBaseDataResponse from a JSON string
routes_knowledgebase_knowledge_base_data_response_instance = RoutesKnowledgebaseKnowledgeBaseDataResponse.from_json(json)
# print the JSON string representation of the object
print(RoutesKnowledgebaseKnowledgeBaseDataResponse.to_json())

# convert the object into a dict
routes_knowledgebase_knowledge_base_data_response_dict = routes_knowledgebase_knowledge_base_data_response_instance.to_dict()
# create an instance of RoutesKnowledgebaseKnowledgeBaseDataResponse from a dict
routes_knowledgebase_knowledge_base_data_response_from_dict = RoutesKnowledgebaseKnowledgeBaseDataResponse.from_dict(routes_knowledgebase_knowledge_base_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


