# MonthYear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | The month of the year. | 
**year** | **int** | The year. | 

## Example

```python
from odin_sdk.models.month_year import MonthYear

# TODO update the JSON string below
json = "{}"
# create an instance of MonthYear from a JSON string
month_year_instance = MonthYear.from_json(json)
# print the JSON string representation of the object
print(MonthYear.to_json())

# convert the object into a dict
month_year_dict = month_year_instance.to_dict()
# create an instance of MonthYear from a dict
month_year_from_dict = MonthYear.from_dict(month_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


