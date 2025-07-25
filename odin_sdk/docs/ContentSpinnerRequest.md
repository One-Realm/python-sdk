# ContentSpinnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_text** | **str** | Input text to create content from. | 
**project_id** | **str** | Project ID in which to run the spinner. | 
**additional_instructions** | **List[str]** |  | [optional] 
**temperature** | **float** |  | [optional] 
**model_name** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.content_spinner_request import ContentSpinnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSpinnerRequest from a JSON string
content_spinner_request_instance = ContentSpinnerRequest.from_json(json)
# print the JSON string representation of the object
print(ContentSpinnerRequest.to_json())

# convert the object into a dict
content_spinner_request_dict = content_spinner_request_instance.to_dict()
# create an instance of ContentSpinnerRequest from a dict
content_spinner_request_from_dict = ContentSpinnerRequest.from_dict(content_spinner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


