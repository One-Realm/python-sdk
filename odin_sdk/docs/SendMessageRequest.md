# SendMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**project_id** | **str** |  | 
**chat_id** | **str** |  | [optional] 
**document_keys** | **List[str]** |  | [optional] 
**google_search** | **bool** |  | [optional] 
**is_test** | **bool** |  | [optional] 
**personality_name** | **str** |  | [optional] 
**return_message** | **bool** |  | [optional] 
**ai_response** | **bool** |  | [optional] 
**model_name** | **str** |  | [optional] 
**agent_type** | **str** |  | [optional] 
**chat_name** | **str** |  | [optional] 
**agent_id** | **str** |  | [optional] 
**personality_id** | **str** |  | [optional] 
**use_knowledgebase** | **bool** |  | [optional] 
**is_regenerating** | **bool** |  | [optional] 
**message_id** | **str** |  | [optional] 
**ui_form** | **object** |  | [optional] 
**images** | **List[bytearray]** |  | [optional] 
**format_instructions** | **str** |  | [optional] 
**ignore_chat_history** | **bool** |  | [optional] 
**example_json** | **str** |  | [optional] 
**is_teams_bot** | **bool** |  | [optional] 
**sent_from_automator** | **bool** |  | [optional] 
**skip_stream** | **bool** |  | [optional] 
**request_metadata** | **object** |  | [optional] 
**artifact** | [**OpenCanvasGraphAnnotation**](OpenCanvasGraphAnnotation.md) |  | [optional] 

## Example

```python
from odin_sdk.models.send_message_request import SendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequest from a JSON string
send_message_request_instance = SendMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequest.to_json())

# convert the object into a dict
send_message_request_dict = send_message_request_instance.to_dict()
# create an instance of SendMessageRequest from a dict
send_message_request_from_dict = SendMessageRequest.from_dict(send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


