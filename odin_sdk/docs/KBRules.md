# KBRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | view permission for kb | [optional] [default to False]
**edit** | **bool** | edit permission for kb | [optional] [default to False]

## Example

```python
from odin_sdk.models.kb_rules import KBRules

# TODO update the JSON string below
json = "{}"
# create an instance of KBRules from a JSON string
kb_rules_instance = KBRules.from_json(json)
# print the JSON string representation of the object
print(KBRules.to_json())

# convert the object into a dict
kb_rules_dict = kb_rules_instance.to_dict()
# create an instance of KBRules from a dict
kb_rules_from_dict = KBRules.from_dict(kb_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


