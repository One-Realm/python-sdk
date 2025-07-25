# GetKbAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type_count** | [**List[DocTypeCount]**](DocTypeCount.md) |  | 
**average_word_count_per_doc** | **float** |  | 
**words_and_docs_added_per_day** | [**List[DailyWordsDocsAdded]**](DailyWordsDocsAdded.md) |  | 
**categories** | [**List[KBCategory]**](KBCategory.md) |  | 
**sources_info** | [**List[SourceInfo]**](SourceInfo.md) |  | 

## Example

```python
from odin_sdk.models.get_kb_analytics_response import GetKbAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKbAnalyticsResponse from a JSON string
get_kb_analytics_response_instance = GetKbAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(GetKbAnalyticsResponse.to_json())

# convert the object into a dict
get_kb_analytics_response_dict = get_kb_analytics_response_instance.to_dict()
# create an instance of GetKbAnalyticsResponse from a dict
get_kb_analytics_response_from_dict = GetKbAnalyticsResponse.from_dict(get_kb_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


