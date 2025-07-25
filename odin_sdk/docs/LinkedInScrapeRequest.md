# LinkedInScrapeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query to search for on LinkedIn | 
**num_links** | **int** | The number of LinkedIn profiles to retrieve (default is 1) | [optional] [default to 1]
**urls_to_exclude** | **List[List[str]]** | List of LinkedIn profile URLs to exclude (optional) | [optional] [default to []]

## Example

```python
from odin_sdk.models.linked_in_scrape_request import LinkedInScrapeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedInScrapeRequest from a JSON string
linked_in_scrape_request_instance = LinkedInScrapeRequest.from_json(json)
# print the JSON string representation of the object
print(LinkedInScrapeRequest.to_json())

# convert the object into a dict
linked_in_scrape_request_dict = linked_in_scrape_request_instance.to_dict()
# create an instance of LinkedInScrapeRequest from a dict
linked_in_scrape_request_from_dict = LinkedInScrapeRequest.from_dict(linked_in_scrape_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


