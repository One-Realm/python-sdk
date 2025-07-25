# SettingsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | view permission for settings | [optional] [default to False]
**edit** | **bool** | edit permission for settings | [optional] [default to False]

## Example

```python
from odin_sdk.models.settings_rules import SettingsRules

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsRules from a JSON string
settings_rules_instance = SettingsRules.from_json(json)
# print the JSON string representation of the object
print(SettingsRules.to_json())

# convert the object into a dict
settings_rules_dict = settings_rules_instance.to_dict()
# create an instance of SettingsRules from a dict
settings_rules_from_dict = SettingsRules.from_dict(settings_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


