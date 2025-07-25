# ChartSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the series | 
**column** | **str** | Column name for the series | 
**aggregation** | **str** | Aggregation function for the series | 
**label** | **str** |  | [optional] 
**count_type** | **str** |  | [optional] 
**condition** | **object** |  | [optional] 
**filters** | **List[object]** |  | [optional] 

## Example

```python
from odin_sdk.models.chart_series import ChartSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSeries from a JSON string
chart_series_instance = ChartSeries.from_json(json)
# print the JSON string representation of the object
print(ChartSeries.to_json())

# convert the object into a dict
chart_series_dict = chart_series_instance.to_dict()
# create an instance of ChartSeries from a dict
chart_series_from_dict = ChartSeries.from_dict(chart_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


