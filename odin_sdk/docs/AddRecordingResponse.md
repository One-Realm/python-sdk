# AddRecordingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**recording_id** | **str** |  | 

## Example

```python
from odin_sdk.models.add_recording_response import AddRecordingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddRecordingResponse from a JSON string
add_recording_response_instance = AddRecordingResponse.from_json(json)
# print the JSON string representation of the object
print(AddRecordingResponse.to_json())

# convert the object into a dict
add_recording_response_dict = add_recording_response_instance.to_dict()
# create an instance of AddRecordingResponse from a dict
add_recording_response_from_dict = AddRecordingResponse.from_dict(add_recording_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


