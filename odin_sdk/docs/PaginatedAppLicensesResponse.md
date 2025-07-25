# PaginatedAppLicensesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**licenses** | [**List[AppLicenseResponse]**](AppLicenseResponse.md) |  | 

## Example

```python
from odin_sdk.models.paginated_app_licenses_response import PaginatedAppLicensesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAppLicensesResponse from a JSON string
paginated_app_licenses_response_instance = PaginatedAppLicensesResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedAppLicensesResponse.to_json())

# convert the object into a dict
paginated_app_licenses_response_dict = paginated_app_licenses_response_instance.to_dict()
# create an instance of PaginatedAppLicensesResponse from a dict
paginated_app_licenses_response_from_dict = PaginatedAppLicensesResponse.from_dict(paginated_app_licenses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


