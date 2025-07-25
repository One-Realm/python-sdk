# MessageFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**question** | **str** |  | 
**answer** | **str** |  | [optional] 
**created_at** | **float** |  | 
**feedback_count** | **int** |  | 
**feedback_arr** | [**List[Feedback]**](Feedback.md) |  | 

## Example

```python
from odin_sdk.models.message_feedback import MessageFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of MessageFeedback from a JSON string
message_feedback_instance = MessageFeedback.from_json(json)
# print the JSON string representation of the object
print(MessageFeedback.to_json())

# convert the object into a dict
message_feedback_dict = message_feedback_instance.to_dict()
# create an instance of MessageFeedback from a dict
message_feedback_from_dict = MessageFeedback.from_dict(message_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


