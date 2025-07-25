# TestApiToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the API request was successful | 
**message** | **str** | A message describing the result | 
**flow_run_id** | **str** |  | [optional] 
**response** | **object** |  | [optional] 
**chat_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.test_api_tool_response import TestApiToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestApiToolResponse from a JSON string
test_api_tool_response_instance = TestApiToolResponse.from_json(json)
# print the JSON string representation of the object
print(TestApiToolResponse.to_json())

# convert the object into a dict
test_api_tool_response_dict = test_api_tool_response_instance.to_dict()
# create an instance of TestApiToolResponse from a dict
test_api_tool_response_from_dict = TestApiToolResponse.from_dict(test_api_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


