# UseTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_id** | **str** |  | 
**template_used** | **str** |  | 

## Example

```python
from odin_sdk.models.use_template_response import UseTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UseTemplateResponse from a JSON string
use_template_response_instance = UseTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(UseTemplateResponse.to_json())

# convert the object into a dict
use_template_response_dict = use_template_response_instance.to_dict()
# create an instance of UseTemplateResponse from a dict
use_template_response_from_dict = UseTemplateResponse.from_dict(use_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


