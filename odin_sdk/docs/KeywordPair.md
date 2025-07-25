# KeywordPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** |  | 
**translation** | **str** |  | 

## Example

```python
from odin_sdk.models.keyword_pair import KeywordPair

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordPair from a JSON string
keyword_pair_instance = KeywordPair.from_json(json)
# print the JSON string representation of the object
print(KeywordPair.to_json())

# convert the object into a dict
keyword_pair_dict = keyword_pair_instance.to_dict()
# create an instance of KeywordPair from a dict
keyword_pair_from_dict = KeywordPair.from_dict(keyword_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


