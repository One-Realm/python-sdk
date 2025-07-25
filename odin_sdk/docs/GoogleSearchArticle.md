# GoogleSearchArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url of the article. | 
**markdown_content** | **str** | The markdown content of the article. | 
**html_content** | **str** | The html content of the article. | 
**title** | **str** | The title of the article. | 
**publish_date** | **str** | The publish date of the article. | 
**author** | **str** | The author of the article. | 

## Example

```python
from odin_sdk.models.google_search_article import GoogleSearchArticle

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSearchArticle from a JSON string
google_search_article_instance = GoogleSearchArticle.from_json(json)
# print the JSON string representation of the object
print(GoogleSearchArticle.to_json())

# convert the object into a dict
google_search_article_dict = google_search_article_instance.to_dict()
# create an instance of GoogleSearchArticle from a dict
google_search_article_from_dict = GoogleSearchArticle.from_dict(google_search_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


