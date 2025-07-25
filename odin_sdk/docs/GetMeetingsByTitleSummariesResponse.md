# GetMeetingsByTitleSummariesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summaries** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.get_meetings_by_title_summaries_response import GetMeetingsByTitleSummariesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeetingsByTitleSummariesResponse from a JSON string
get_meetings_by_title_summaries_response_instance = GetMeetingsByTitleSummariesResponse.from_json(json)
# print the JSON string representation of the object
print(GetMeetingsByTitleSummariesResponse.to_json())

# convert the object into a dict
get_meetings_by_title_summaries_response_dict = get_meetings_by_title_summaries_response_instance.to_dict()
# create an instance of GetMeetingsByTitleSummariesResponse from a dict
get_meetings_by_title_summaries_response_from_dict = GetMeetingsByTitleSummariesResponse.from_dict(get_meetings_by_title_summaries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


