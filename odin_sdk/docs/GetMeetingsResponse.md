# GetMeetingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meetings** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.get_meetings_response import GetMeetingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeetingsResponse from a JSON string
get_meetings_response_instance = GetMeetingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMeetingsResponse.to_json())

# convert the object into a dict
get_meetings_response_dict = get_meetings_response_instance.to_dict()
# create an instance of GetMeetingsResponse from a dict
get_meetings_response_from_dict = GetMeetingsResponse.from_dict(get_meetings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


