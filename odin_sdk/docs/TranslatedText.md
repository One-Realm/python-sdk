# TranslatedText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** |  | 
**translation** | **str** |  | 

## Example

```python
from odin_sdk.models.translated_text import TranslatedText

# TODO update the JSON string below
json = "{}"
# create an instance of TranslatedText from a JSON string
translated_text_instance = TranslatedText.from_json(json)
# print the JSON string representation of the object
print(TranslatedText.to_json())

# convert the object into a dict
translated_text_dict = translated_text_instance.to_dict()
# create an instance of TranslatedText from a dict
translated_text_from_dict = TranslatedText.from_dict(translated_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


