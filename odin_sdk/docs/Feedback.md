# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**feedback_type** | **str** |  | 
**details** | **str** |  | 

## Example

```python
from odin_sdk.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print(Feedback.to_json())

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_from_dict = Feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


