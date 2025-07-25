# RoutesProjectsResponseKBDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the document. | 
**content_key** | **str** | The content key of the document - either full URL in case of web links stored in the KB or full filename, e.g. &#39;example.pdf&#39;. | 
**content** | **str** |  | [optional] 
**metadata** | **object** | The metadata of the document. | 
**doc_type** | **str** | The type of the document. | 
**metadata_extracted** | **object** |  | [optional] 
**pii** | **object** |  | [optional] 
**data_type** | **object** |  | [optional] 
**data_type_id** | **str** |  | [optional] 
**data_type_name** | **str** |  | [optional] 
**data_type_extracted** | **object** |  | [optional] 
**document_id** | **str** |  | [optional] 
**extraction_with_comparison** | **List[object]** |  | [optional] 
**extraction_with_confidence_from_llm** | **List[object]** |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_response_kb_document import RoutesProjectsResponseKBDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsResponseKBDocument from a JSON string
routes_projects_response_kb_document_instance = RoutesProjectsResponseKBDocument.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsResponseKBDocument.to_json())

# convert the object into a dict
routes_projects_response_kb_document_dict = routes_projects_response_kb_document_instance.to_dict()
# create an instance of RoutesProjectsResponseKBDocument from a dict
routes_projects_response_kb_document_from_dict = RoutesProjectsResponseKBDocument.from_dict(routes_projects_response_kb_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


