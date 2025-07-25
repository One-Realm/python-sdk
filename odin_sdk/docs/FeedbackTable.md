# FeedbackTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedbacks** | [**List[MessageInfo]**](MessageInfo.md) |  | 

## Example

```python
from odin_sdk.models.feedback_table import FeedbackTable

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackTable from a JSON string
feedback_table_instance = FeedbackTable.from_json(json)
# print the JSON string representation of the object
print(FeedbackTable.to_json())

# convert the object into a dict
feedback_table_dict = feedback_table_instance.to_dict()
# create an instance of FeedbackTable from a dict
feedback_table_from_dict = FeedbackTable.from_dict(feedback_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


