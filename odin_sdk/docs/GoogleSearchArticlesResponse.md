# GoogleSearchArticlesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GoogleSearchArticle]**](GoogleSearchArticle.md) | The results of the search. | [optional] [default to []]

## Example

```python
from odin_sdk.models.google_search_articles_response import GoogleSearchArticlesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSearchArticlesResponse from a JSON string
google_search_articles_response_instance = GoogleSearchArticlesResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleSearchArticlesResponse.to_json())

# convert the object into a dict
google_search_articles_response_dict = google_search_articles_response_instance.to_dict()
# create an instance of GoogleSearchArticlesResponse from a dict
google_search_articles_response_from_dict = GoogleSearchArticlesResponse.from_dict(google_search_articles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


