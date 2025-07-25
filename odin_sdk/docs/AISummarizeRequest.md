# AISummarizeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**project_id** | **str** |  | 
**instructions** | **str** |  | 

## Example

```python
from odin_sdk.models.ai_summarize_request import AISummarizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AISummarizeRequest from a JSON string
ai_summarize_request_instance = AISummarizeRequest.from_json(json)
# print the JSON string representation of the object
print(AISummarizeRequest.to_json())

# convert the object into a dict
ai_summarize_request_dict = ai_summarize_request_instance.to_dict()
# create an instance of AISummarizeRequest from a dict
ai_summarize_request_from_dict = AISummarizeRequest.from_dict(ai_summarize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


