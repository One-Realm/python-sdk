# ExtractYoutubeCaptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** |  | 

## Example

```python
from odin_sdk.models.extract_youtube_captions_request import ExtractYoutubeCaptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractYoutubeCaptionsRequest from a JSON string
extract_youtube_captions_request_instance = ExtractYoutubeCaptionsRequest.from_json(json)
# print the JSON string representation of the object
print(ExtractYoutubeCaptionsRequest.to_json())

# convert the object into a dict
extract_youtube_captions_request_dict = extract_youtube_captions_request_instance.to_dict()
# create an instance of ExtractYoutubeCaptionsRequest from a dict
extract_youtube_captions_request_from_dict = ExtractYoutubeCaptionsRequest.from_dict(extract_youtube_captions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


