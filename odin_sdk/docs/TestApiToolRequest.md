# TestApiToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The ID of the project | 
**config** | **object** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**ui_form** | **object** | The UI form data to use for the API request | 
**chat_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.test_api_tool_request import TestApiToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestApiToolRequest from a JSON string
test_api_tool_request_instance = TestApiToolRequest.from_json(json)
# print the JSON string representation of the object
print(TestApiToolRequest.to_json())

# convert the object into a dict
test_api_tool_request_dict = test_api_tool_request_instance.to_dict()
# create an instance of TestApiToolRequest from a dict
test_api_tool_request_from_dict = TestApiToolRequest.from_dict(test_api_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


