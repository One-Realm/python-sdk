# TemplatePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**fields_count** | **int** |  | 
**preview_fields** | [**List[TemplateField]**](TemplateField.md) |  | [optional] [default to []]
**category** | **str** |  | 

## Example

```python
from odin_sdk.models.template_preview import TemplatePreview

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePreview from a JSON string
template_preview_instance = TemplatePreview.from_json(json)
# print the JSON string representation of the object
print(TemplatePreview.to_json())

# convert the object into a dict
template_preview_dict = template_preview_instance.to_dict()
# create an instance of TemplatePreview from a dict
template_preview_from_dict = TemplatePreview.from_dict(template_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


