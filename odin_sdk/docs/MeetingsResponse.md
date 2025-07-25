# MeetingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meetings** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.meetings_response import MeetingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeetingsResponse from a JSON string
meetings_response_instance = MeetingsResponse.from_json(json)
# print the JSON string representation of the object
print(MeetingsResponse.to_json())

# convert the object into a dict
meetings_response_dict = meetings_response_instance.to_dict()
# create an instance of MeetingsResponse from a dict
meetings_response_from_dict = MeetingsResponse.from_dict(meetings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


