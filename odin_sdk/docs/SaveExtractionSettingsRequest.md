# SaveExtractionSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pii_masking_enabled** | **bool** | Whether PII masking is enabled | [optional] [default to False]
**custom_extraction_config** | **List[object]** |  | [optional] 
**extraction_results** | **List[object]** |  | [optional] 
**sample_document_id** | **str** |  | [optional] 
**apply_re_validation** | **bool** | Whether to apply re-validation | [optional] [default to False]

## Example

```python
from odin_sdk.models.save_extraction_settings_request import SaveExtractionSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveExtractionSettingsRequest from a JSON string
save_extraction_settings_request_instance = SaveExtractionSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SaveExtractionSettingsRequest.to_json())

# convert the object into a dict
save_extraction_settings_request_dict = save_extraction_settings_request_instance.to_dict()
# create an instance of SaveExtractionSettingsRequest from a dict
save_extraction_settings_request_from_dict = SaveExtractionSettingsRequest.from_dict(save_extraction_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


