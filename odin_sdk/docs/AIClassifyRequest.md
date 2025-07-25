# AIClassifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**model_name** | **str** |  | [optional] 
**categories** | [**List[CategoryInput]**](CategoryInput.md) |  | [optional] 

## Example

```python
from odin_sdk.models.ai_classify_request import AIClassifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AIClassifyRequest from a JSON string
ai_classify_request_instance = AIClassifyRequest.from_json(json)
# print the JSON string representation of the object
print(AIClassifyRequest.to_json())

# convert the object into a dict
ai_classify_request_dict = ai_classify_request_instance.to_dict()
# create an instance of AIClassifyRequest from a dict
ai_classify_request_from_dict = AIClassifyRequest.from_dict(ai_classify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


