# AppLicenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats** | **int** |  | [optional] 
**credits** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**plan_type** | **str** |  | [optional] 
**license_key** | **str** |  | 
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**used** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.app_license_response import AppLicenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppLicenseResponse from a JSON string
app_license_response_instance = AppLicenseResponse.from_json(json)
# print the JSON string representation of the object
print(AppLicenseResponse.to_json())

# convert the object into a dict
app_license_response_dict = app_license_response_instance.to_dict()
# create an instance of AppLicenseResponse from a dict
app_license_response_from_dict = AppLicenseResponse.from_dict(app_license_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


