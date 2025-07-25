# ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost


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
from odin_sdk.models.response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post import ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost from a JSON string
response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post_instance = ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost.from_json(json)
# print the JSON string representation of the object
print(ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost.to_json())

# convert the object into a dict
response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post_dict = response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post_instance.to_dict()
# create an instance of ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost from a dict
response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post_from_dict = ResponseAddConfluencePageToKnowledgeBaseProjectKnowledgeAddConfluencePost.from_dict(response_add_confluence_page_to_knowledge_base_project_knowledge_add_confluence_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


