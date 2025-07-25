# ExecuteScriptResponse

Response model for script execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**result** | [**AnyOf**](AnyOf.md) |  | [optional] 
**error** | **str** |  | [optional] 
**execution_time_ms** | **int** |  | [optional] 
**version** | **str** |  | 
**lambda_function_name** | **str** |  | 
**execution_id** | **int** |  | [optional] 
**stdout** | **str** |  | [optional] 
**stderr** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.execute_script_response import ExecuteScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteScriptResponse from a JSON string
execute_script_response_instance = ExecuteScriptResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteScriptResponse.to_json())

# convert the object into a dict
execute_script_response_dict = execute_script_response_instance.to_dict()
# create an instance of ExecuteScriptResponse from a dict
execute_script_response_from_dict = ExecuteScriptResponse.from_dict(execute_script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


