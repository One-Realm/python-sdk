# GetDashboardDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data** | **object** | Dictionary with widget_id as key and widget data as value | 

## Example

```python
from odin_sdk.models.get_dashboard_data_response import GetDashboardDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardDataResponse from a JSON string
get_dashboard_data_response_instance = GetDashboardDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetDashboardDataResponse.to_json())

# convert the object into a dict
get_dashboard_data_response_dict = get_dashboard_data_response_instance.to_dict()
# create an instance of GetDashboardDataResponse from a dict
get_dashboard_data_response_from_dict = GetDashboardDataResponse.from_dict(get_dashboard_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


