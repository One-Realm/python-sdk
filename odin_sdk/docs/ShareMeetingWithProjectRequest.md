# ShareMeetingWithProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_id** | **str** |  | 
**project_ids** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.share_meeting_with_project_request import ShareMeetingWithProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareMeetingWithProjectRequest from a JSON string
share_meeting_with_project_request_instance = ShareMeetingWithProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ShareMeetingWithProjectRequest.to_json())

# convert the object into a dict
share_meeting_with_project_request_dict = share_meeting_with_project_request_instance.to_dict()
# create an instance of ShareMeetingWithProjectRequest from a dict
share_meeting_with_project_request_from_dict = ShareMeetingWithProjectRequest.from_dict(share_meeting_with_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


