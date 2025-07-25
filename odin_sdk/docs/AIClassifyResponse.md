# AIClassifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**reason** | **str** |  | 

## Example

```python
from odin_sdk.models.ai_classify_response import AIClassifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIClassifyResponse from a JSON string
ai_classify_response_instance = AIClassifyResponse.from_json(json)
# print the JSON string representation of the object
print(AIClassifyResponse.to_json())

# convert the object into a dict
ai_classify_response_dict = ai_classify_response_instance.to_dict()
# create an instance of AIClassifyResponse from a dict
ai_classify_response_from_dict = AIClassifyResponse.from_dict(ai_classify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


