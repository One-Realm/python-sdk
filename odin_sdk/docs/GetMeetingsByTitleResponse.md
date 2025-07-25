# GetMeetingsByTitleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meetings** | [**List[MeetingData]**](MeetingData.md) |  | 

## Example

```python
from odin_sdk.models.get_meetings_by_title_response import GetMeetingsByTitleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeetingsByTitleResponse from a JSON string
get_meetings_by_title_response_instance = GetMeetingsByTitleResponse.from_json(json)
# print the JSON string representation of the object
print(GetMeetingsByTitleResponse.to_json())

# convert the object into a dict
get_meetings_by_title_response_dict = get_meetings_by_title_response_instance.to_dict()
# create an instance of GetMeetingsByTitleResponse from a dict
get_meetings_by_title_response_from_dict = GetMeetingsByTitleResponse.from_dict(get_meetings_by_title_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


