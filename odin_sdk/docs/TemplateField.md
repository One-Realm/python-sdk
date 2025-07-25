# TemplateField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from odin_sdk.models.template_field import TemplateField

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateField from a JSON string
template_field_instance = TemplateField.from_json(json)
# print the JSON string representation of the object
print(TemplateField.to_json())

# convert the object into a dict
template_field_dict = template_field_instance.to_dict()
# create an instance of TemplateField from a dict
template_field_from_dict = TemplateField.from_dict(template_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


