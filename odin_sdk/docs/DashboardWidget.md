# DashboardWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the widget | 
**type** | [**DashboardWidgetType**](DashboardWidgetType.md) | Type of the widget | 
**title** | **str** | Display title for the widget | 
**config** | [**DashboardWidgetConfig**](DashboardWidgetConfig.md) | Widget configuration | 

## Example

```python
from odin_sdk.models.dashboard_widget import DashboardWidget

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWidget from a JSON string
dashboard_widget_instance = DashboardWidget.from_json(json)
# print the JSON string representation of the object
print(DashboardWidget.to_json())

# convert the object into a dict
dashboard_widget_dict = dashboard_widget_instance.to_dict()
# create an instance of DashboardWidget from a dict
dashboard_widget_from_dict = DashboardWidget.from_dict(dashboard_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


