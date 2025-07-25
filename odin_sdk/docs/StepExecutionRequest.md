# StepExecutionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | 
**tool_id** | **str** | The tool ID to save results to | 
**step_id** | **str** | The step ID to execute | 
**tool_config** | **object** | The complete tool configuration | 

## Example

```python
from odin_sdk.models.step_execution_request import StepExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StepExecutionRequest from a JSON string
step_execution_request_instance = StepExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(StepExecutionRequest.to_json())

# convert the object into a dict
step_execution_request_dict = step_execution_request_instance.to_dict()
# create an instance of StepExecutionRequest from a dict
step_execution_request_from_dict = StepExecutionRequest.from_dict(step_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


