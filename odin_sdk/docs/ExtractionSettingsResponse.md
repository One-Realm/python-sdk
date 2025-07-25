# ExtractionSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**settings** | **object** |  | 

## Example

```python
from odin_sdk.models.extraction_settings_response import ExtractionSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionSettingsResponse from a JSON string
extraction_settings_response_instance = ExtractionSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractionSettingsResponse.to_json())

# convert the object into a dict
extraction_settings_response_dict = extraction_settings_response_instance.to_dict()
# create an instance of ExtractionSettingsResponse from a dict
extraction_settings_response_from_dict = ExtractionSettingsResponse.from_dict(extraction_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


