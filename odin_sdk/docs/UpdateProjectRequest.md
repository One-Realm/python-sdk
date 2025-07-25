# UpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**enrich_question** | **bool** |  | [optional] 
**enrich_sources** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**test_info** | **object** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**no_context_answer** | **str** |  | [optional] 
**only_answer_with_context** | **bool** |  | [optional] 
**custom_chatbot** | **object** |  | [optional] 
**use_textract** | **bool** |  | [optional] 
**mask_pii** | **bool** |  | [optional] 
**inline_citations** | **bool** |  | [optional] 
**data_extraction_method** | **str** |  | [optional] 
**teamsbot_upload_method** | **str** |  | [optional] 
**teamsbot_static_message_footer** | **str** |  | [optional] 
**teamsbot_show_feedback_buttons** | **bool** |  | [optional] 
**teamsbot_show_kb_search_message** | **bool** |  | [optional] 
**teamsbot_show_message_sources** | **bool** |  | [optional] 
**enable_temporary_message_retention** | **bool** |  | [optional] 
**temporary_message_retention_duration** | **int** |  | [optional] 
**docx_extraction_method** | **str** |  | [optional] 
**shared_to_team** | **bool** |  | [optional] 
**team_default_role** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectRequest.to_json())

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_from_dict = UpdateProjectRequest.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


