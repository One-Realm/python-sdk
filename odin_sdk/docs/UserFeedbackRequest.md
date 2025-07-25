# UserFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_feedback** | **bool** |  | [optional] 
**message_id** | **str** |  | 
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**additional_feedback** | **bool** |  | [optional] 
**is_correct_answer_option** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**unit_test_existing_group_id** | **str** |  | [optional] 
**new_unit_test_group_name** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**expected_answer** | **str** |  | [optional] 
**is_incorrect_answer_option** | **bool** |  | [optional] 
**suggested_better_response** | **str** |  | [optional] 
**is_incorrect_source_url_option** | **bool** |  | [optional] 
**correct_source_url** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.user_feedback_request import UserFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeedbackRequest from a JSON string
user_feedback_request_instance = UserFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(UserFeedbackRequest.to_json())

# convert the object into a dict
user_feedback_request_dict = user_feedback_request_instance.to_dict()
# create an instance of UserFeedbackRequest from a dict
user_feedback_request_from_dict = UserFeedbackRequest.from_dict(user_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


