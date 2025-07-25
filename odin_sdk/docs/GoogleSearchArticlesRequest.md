# GoogleSearchArticlesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query to search for. | 
**max_results** | **int** | The maximum number of results to return. | [optional] [default to 5]
**download_pages** | **bool** | Whether to download the pages or not. | [optional] [default to False]
**search_type** | **str** | The search type. Currently all or news is supported. | [optional] [default to 'google']
**website_white_list** | **List[str]** | The list of websites to limit the search to. | [optional] [default to []]
**limit_date_range** | **bool** |  | [optional] 
**date_range_start** | **float** |  | [optional] 
**date_range_end** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.google_search_articles_request import GoogleSearchArticlesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSearchArticlesRequest from a JSON string
google_search_articles_request_instance = GoogleSearchArticlesRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleSearchArticlesRequest.to_json())

# convert the object into a dict
google_search_articles_request_dict = google_search_articles_request_instance.to_dict()
# create an instance of GoogleSearchArticlesRequest from a dict
google_search_articles_request_from_dict = GoogleSearchArticlesRequest.from_dict(google_search_articles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


