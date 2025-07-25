# UIForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** |  | 
**action_fields** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.ui_form import UIForm

# TODO update the JSON string below
json = "{}"
# create an instance of UIForm from a JSON string
ui_form_instance = UIForm.from_json(json)
# print the JSON string representation of the object
print(UIForm.to_json())

# convert the object into a dict
ui_form_dict = ui_form_instance.to_dict()
# create an instance of UIForm from a dict
ui_form_from_dict = UIForm.from_dict(ui_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


