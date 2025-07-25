# EvalTaskInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_keys** | **List[str]** |  | [optional] 
**num_questions** | **int** | The number of questions to generate | 

## Example

```python
from odin_sdk.models.eval_task_input import EvalTaskInput

# TODO update the JSON string below
json = "{}"
# create an instance of EvalTaskInput from a JSON string
eval_task_input_instance = EvalTaskInput.from_json(json)
# print the JSON string representation of the object
print(EvalTaskInput.to_json())

# convert the object into a dict
eval_task_input_dict = eval_task_input_instance.to_dict()
# create an instance of EvalTaskInput from a dict
eval_task_input_from_dict = EvalTaskInput.from_dict(eval_task_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


