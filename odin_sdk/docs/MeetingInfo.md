# MeetingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**ical_uid** | **str** |  | 
**is_recurring** | **bool** |  | 
**visibility** | **str** |  | [optional] 
**webex_invite** | **str** |  | [optional] 
**override_should_record** | **bool** |  | [optional] 
**end_time** | **str** |  | 
**id** | **str** |  | 
**meeting_platform** | **str** |  | 
**calendar_platform** | **str** |  | 
**is_hosted_by_me** | **bool** |  | 
**attendees_emails** | **List[str]** |  | [optional] 
**attendees** | [**List[Attendee]**](Attendee.md) |  | [optional] 
**organizer_email** | **str** |  | 
**teams_invite** | **str** |  | [optional] 
**bot_id** | **str** |  | 
**platform** | **str** |  | 
**meet_invite** | **object** |  | 
**is_external** | **bool** |  | 
**zoom_invite** | **str** |  | [optional] 
**will_record_reason** | **str** |  | 
**will_record** | **bool** |  | 
**start_time** | **str** |  | 

## Example

```python
from odin_sdk.models.meeting_info import MeetingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingInfo from a JSON string
meeting_info_instance = MeetingInfo.from_json(json)
# print the JSON string representation of the object
print(MeetingInfo.to_json())

# convert the object into a dict
meeting_info_dict = meeting_info_instance.to_dict()
# create an instance of MeetingInfo from a dict
meeting_info_from_dict = MeetingInfo.from_dict(meeting_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


