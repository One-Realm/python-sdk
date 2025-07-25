# GetMeetingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_timestamp** | **float** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**timestamp** | **float** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.get_meetings_request import GetMeetingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeetingsRequest from a JSON string
get_meetings_request_instance = GetMeetingsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMeetingsRequest.to_json())

# convert the object into a dict
get_meetings_request_dict = get_meetings_request_instance.to_dict()
# create an instance of GetMeetingsRequest from a dict
get_meetings_request_from_dict = GetMeetingsRequest.from_dict(get_meetings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


