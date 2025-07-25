# ExportStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **str** |  | 
**status** | **str** |  | 
**message** | **str** |  | 
**download_available** | **bool** |  | [optional] [default to False]

## Example

```python
from odin_sdk.models.export_status_response import ExportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportStatusResponse from a JSON string
export_status_response_instance = ExportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ExportStatusResponse.to_json())

# convert the object into a dict
export_status_response_dict = export_status_response_instance.to_dict()
# create an instance of ExportStatusResponse from a dict
export_status_response_from_dict = ExportStatusResponse.from_dict(export_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


