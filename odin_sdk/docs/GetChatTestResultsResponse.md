# GetChatTestResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.get_chat_test_results_response import GetChatTestResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatTestResultsResponse from a JSON string
get_chat_test_results_response_instance = GetChatTestResultsResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatTestResultsResponse.to_json())

# convert the object into a dict
get_chat_test_results_response_dict = get_chat_test_results_response_instance.to_dict()
# create an instance of GetChatTestResultsResponse from a dict
get_chat_test_results_response_from_dict = GetChatTestResultsResponse.from_dict(get_chat_test_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


