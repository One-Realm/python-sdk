# UpdateAnalyticsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_analytics_rules import UpdateAnalyticsRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnalyticsRules from a JSON string
update_analytics_rules_instance = UpdateAnalyticsRules.from_json(json)
# print the JSON string representation of the object
print(UpdateAnalyticsRules.to_json())

# convert the object into a dict
update_analytics_rules_dict = update_analytics_rules_instance.to_dict()
# create an instance of UpdateAnalyticsRules from a dict
update_analytics_rules_from_dict = UpdateAnalyticsRules.from_dict(update_analytics_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


