# UseTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | Name of the template file (without .json extension) | 
**custom_title** | **str** | Custom title for the new data type | 

## Example

```python
from odin_sdk.models.use_template_request import UseTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UseTemplateRequest from a JSON string
use_template_request_instance = UseTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UseTemplateRequest.to_json())

# convert the object into a dict
use_template_request_dict = use_template_request_instance.to_dict()
# create an instance of UseTemplateRequest from a dict
use_template_request_from_dict = UseTemplateRequest.from_dict(use_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


