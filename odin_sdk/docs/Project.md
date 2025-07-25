# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**owner** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**members** | [**List[RoutesProjectsMember]**](RoutesProjectsMember.md) |  | 
**description** | **str** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**kb_info** | [**KbInfo**](KbInfo.md) |  | [optional] 
**kb_last_synced** | **float** |  | [optional] 
**kb_status** | **str** |  | [optional] 
**kb_sync_schedule** | **float** |  | [optional] 
**blacklisted_docs** | **List[str]** |  | [optional] 
**team_id** | **str** |  | [optional] 
**system_prompt** | [**AnyOf**](AnyOf.md) |  | [optional] 
**custom_agent** | **str** |  | [optional] 
**custom_agent_name** | **str** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**use_textract** | **bool** |  | [optional] 
**mask_pii** | **bool** |  | [optional] 
**inline_citations** | **bool** |  | [optional] 
**custom_chatbot** | [**CustomChatbot**](CustomChatbot.md) |  | [optional] 
**feedback_history** | **List[object]** |  | [optional] 
**api_keys** | [**APIKey**](APIKey.md) |  | [optional] 
**kb_version** | **int** |  | [optional] 
**embedding_model** | **str** |  | [optional] 
**teamsbot_upload_method** | **str** |  | [optional] 
**teamsbot_static_message_footer** | **str** |  | [optional] 
**teamsbot_show_feedback_buttons** | **bool** |  | [optional] 
**teamsbot_show_kb_search_message** | **bool** |  | [optional] 
**teamsbot_show_message_sources** | **bool** |  | [optional] 
**shared_to_team** | **bool** |  | [optional] 
**team_default_role** | **str** |  | [optional] 
**shared** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


