# MeetingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_size** | **float** |  | 
**credits_used** | **int** |  | 
**odin_attendees** | **List[object]** |  | [optional] 
**is_calendar_meeting** | **bool** |  | 
**meeting_url** | **object** |  | [optional] 
**media_retention_end** | **str** |  | [optional] 
**attendee_emails** | **List[str]** |  | 
**status_code** | **str** |  | 
**video_url** | **str** |  | 
**meeting_info** | [**MeetingInfo**](MeetingInfo.md) |  | 
**join_at** | **str** |  | [optional] 
**video_size** | **float** |  | 
**calendar_meetings** | **List[object]** |  | 
**timestamp** | **float** |  | 
**meeting_participants** | **List[object]** |  | 
**recording** | **str** |  | [optional] 
**meeting_duration** | **float** |  | 
**meeting_metadata** | **str** |  | [optional] 
**status_changes** | [**List[StatusChange]**](StatusChange.md) |  | 
**id** | **str** |  | 

## Example

```python
from odin_sdk.models.meeting_data import MeetingData

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingData from a JSON string
meeting_data_instance = MeetingData.from_json(json)
# print the JSON string representation of the object
print(MeetingData.to_json())

# convert the object into a dict
meeting_data_dict = meeting_data_instance.to_dict()
# create an instance of MeetingData from a dict
meeting_data_from_dict = MeetingData.from_dict(meeting_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


