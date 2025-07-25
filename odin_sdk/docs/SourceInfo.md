# SourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**usage_percentage** | **float** |  | 
**faqs** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.source_info import SourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SourceInfo from a JSON string
source_info_instance = SourceInfo.from_json(json)
# print the JSON string representation of the object
print(SourceInfo.to_json())

# convert the object into a dict
source_info_dict = source_info_instance.to_dict()
# create an instance of SourceInfo from a dict
source_info_from_dict = SourceInfo.from_dict(source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


