# TestExecuteResponse

Response model for test execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**result** | [**AnyOf**](AnyOf.md) |  | [optional] 
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**error_traceback** | **str** |  | [optional] 
**execution_time_ms** | **int** |  | [optional] 
**memory_used_mb** | **int** |  | [optional] 
**logs** | **str** |  | [optional] 
**function_name** | **str** |  | 
**stdout** | **str** |  | [optional] 
**stderr** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.test_execute_response import TestExecuteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestExecuteResponse from a JSON string
test_execute_response_instance = TestExecuteResponse.from_json(json)
# print the JSON string representation of the object
print(TestExecuteResponse.to_json())

# convert the object into a dict
test_execute_response_dict = test_execute_response_instance.to_dict()
# create an instance of TestExecuteResponse from a dict
test_execute_response_from_dict = TestExecuteResponse.from_dict(test_execute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


