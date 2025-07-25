# DeleteQuestionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_question_output import DeleteQuestionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteQuestionOutput from a JSON string
delete_question_output_instance = DeleteQuestionOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteQuestionOutput.to_json())

# convert the object into a dict
delete_question_output_dict = delete_question_output_instance.to_dict()
# create an instance of DeleteQuestionOutput from a dict
delete_question_output_from_dict = DeleteQuestionOutput.from_dict(delete_question_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


