# UpdateSettingsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_settings_rules import UpdateSettingsRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSettingsRules from a JSON string
update_settings_rules_instance = UpdateSettingsRules.from_json(json)
# print the JSON string representation of the object
print(UpdateSettingsRules.to_json())

# convert the object into a dict
update_settings_rules_dict = update_settings_rules_instance.to_dict()
# create an instance of UpdateSettingsRules from a dict
update_settings_rules_from_dict = UpdateSettingsRules.from_dict(update_settings_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


