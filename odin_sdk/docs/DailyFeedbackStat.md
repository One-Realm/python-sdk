# DailyFeedbackStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correct_answer_option_count** | **int** |  | 
**incorrect_answer_option_count** | **int** |  | 
**incorrect_source_url_option_count** | **int** |  | 

## Example

```python
from odin_sdk.models.daily_feedback_stat import DailyFeedbackStat

# TODO update the JSON string below
json = "{}"
# create an instance of DailyFeedbackStat from a JSON string
daily_feedback_stat_instance = DailyFeedbackStat.from_json(json)
# print the JSON string representation of the object
print(DailyFeedbackStat.to_json())

# convert the object into a dict
daily_feedback_stat_dict = daily_feedback_stat_instance.to_dict()
# create an instance of DailyFeedbackStat from a dict
daily_feedback_stat_from_dict = DailyFeedbackStat.from_dict(daily_feedback_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


