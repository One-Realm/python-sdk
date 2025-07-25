# AppLicenseUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats** | **int** |  | [optional] 
**credits** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.app_license_update import AppLicenseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AppLicenseUpdate from a JSON string
app_license_update_instance = AppLicenseUpdate.from_json(json)
# print the JSON string representation of the object
print(AppLicenseUpdate.to_json())

# convert the object into a dict
app_license_update_dict = app_license_update_instance.to_dict()
# create an instance of AppLicenseUpdate from a dict
app_license_update_from_dict = AppLicenseUpdate.from_dict(app_license_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


