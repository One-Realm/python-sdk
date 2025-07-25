# ProjectSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**query** | **str** |  | 
**document_keys** | **List[str]** |  | [optional] 
**hybrid_search_lambda** | **float** |  | [optional] [default to 0.1]
**score_threshold** | **float** |  | [optional] [default to 0.1]
**kw_fuzzy_threshold** | **float** |  | [optional] [default to 80]
**kw_curve_multihit** | **bool** |  | [optional] 
**metadata_filters** | [**ProjectSearchMetadata**](ProjectSearchMetadata.md) |  | [optional] 
**max_results** | **int** |  | [optional] 
**full_content_words_limit** | **int** |  | [optional] 
**metadata_weighting** | **float** |  | [optional] 
**remove_duplicates** | **bool** |  | [optional] 
**page** | **int** |  | [optional] 
**debug** | **bool** |  | [optional] 
**generate_ai_summary** | **bool** |  | [optional] 
**search_by_titles** | **bool** |  | [optional] 
**group_on_backend** | **bool** |  | [optional] 
**multihit_weighting** | **float** |  | [optional] 
**add_bonus_from_full_content** | **bool** |  | [optional] 
**bonus_from_full_content_threshold** | **float** |  | [optional] 
**bonus_from_full_content_size** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.project_search_request import ProjectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchRequest from a JSON string
project_search_request_instance = ProjectSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectSearchRequest.to_json())

# convert the object into a dict
project_search_request_dict = project_search_request_instance.to_dict()
# create an instance of ProjectSearchRequest from a dict
project_search_request_from_dict = ProjectSearchRequest.from_dict(project_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


