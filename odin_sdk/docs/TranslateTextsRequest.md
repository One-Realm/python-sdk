# TranslateTextsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_language** | **str** |  | 
**target_language** | **str** |  | 
**texts** | **List[str]** |  | 
**keywords** | [**List[KeywordPair]**](KeywordPair.md) |  | [optional] 
**project_id** | **str** |  | 
**translation_tone** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.translate_texts_request import TranslateTextsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTextsRequest from a JSON string
translate_texts_request_instance = TranslateTextsRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateTextsRequest.to_json())

# convert the object into a dict
translate_texts_request_dict = translate_texts_request_instance.to_dict()
# create an instance of TranslateTextsRequest from a dict
translate_texts_request_from_dict = TranslateTextsRequest.from_dict(translate_texts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


