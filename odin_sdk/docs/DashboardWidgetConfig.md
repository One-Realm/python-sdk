# DashboardWidgetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**chart_type** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**group_by_columns** | **List[str]** |  | [optional] 
**aggregation** | **str** |  | [optional] 
**series** | [**List[ChartSeries]**](ChartSeries.md) |  | [optional] 
**text_content** | **str** |  | [optional] 
**filters** | **List[object]** |  | [optional] 
**operation** | **str** |  | [optional] 
**count_type** | **str** |  | [optional] 
**condition** | **object** |  | [optional] 
**math_enabled** | **bool** |  | [optional] 
**math_operation** | **str** |  | [optional] 
**second_value_source** | **str** |  | [optional] 
**second_value_fixed** | **float** |  | [optional] 
**second_value_column** | **str** |  | [optional] 
**second_value_operation** | **str** |  | [optional] 
**second_value_widget_id** | **str** |  | [optional] 
**second_filters** | **List[object]** |  | [optional] 
**data_source** | **str** |  | [optional] 
**date_grouping** | [**Dict[str, DateGroupingConfig]**](DateGroupingConfig.md) |  | [optional] 
**inherit_dashboard_period** | **bool** |  | [optional] 
**compare_last_period** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.dashboard_widget_config import DashboardWidgetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardWidgetConfig from a JSON string
dashboard_widget_config_instance = DashboardWidgetConfig.from_json(json)
# print the JSON string representation of the object
print(DashboardWidgetConfig.to_json())

# convert the object into a dict
dashboard_widget_config_dict = dashboard_widget_config_instance.to_dict()
# create an instance of DashboardWidgetConfig from a dict
dashboard_widget_config_from_dict = DashboardWidgetConfig.from_dict(dashboard_widget_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


