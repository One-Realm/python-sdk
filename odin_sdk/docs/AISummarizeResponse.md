# AISummarizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.ai_summarize_response import AISummarizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AISummarizeResponse from a JSON string
ai_summarize_response_instance = AISummarizeResponse.from_json(json)
# print the JSON string representation of the object
print(AISummarizeResponse.to_json())

# convert the object into a dict
ai_summarize_response_dict = ai_summarize_response_instance.to_dict()
# create an instance of AISummarizeResponse from a dict
ai_summarize_response_from_dict = AISummarizeResponse.from_dict(ai_summarize_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


