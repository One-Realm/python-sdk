# DateGroupingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Date grouping type: day, week, month, quarter, year | 
**format** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.date_grouping_config import DateGroupingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DateGroupingConfig from a JSON string
date_grouping_config_instance = DateGroupingConfig.from_json(json)
# print the JSON string representation of the object
print(DateGroupingConfig.to_json())

# convert the object into a dict
date_grouping_config_dict = date_grouping_config_instance.to_dict()
# create an instance of DateGroupingConfig from a dict
date_grouping_config_from_dict = DateGroupingConfig.from_dict(date_grouping_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


