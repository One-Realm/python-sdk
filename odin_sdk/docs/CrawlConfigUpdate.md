# CrawlConfigUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_name** | **str** |  | 
**root_url** | **str** |  | 
**repeat** | **float** |  | [optional] 
**limit_to_root_domain** | **bool** |  | [optional] [default to False]
**limit_to_domains** | **List[str]** |  | [optional] [default to []]
**limit_to_patterns** | **List[str]** |  | [optional] [default to []]
**download_files** | **bool** |  | [optional] [default to False]
**max_depth** | **int** |  | [optional] [default to 5]
**max_pages** | **int** |  | [optional] [default to 1000]
**strategy** | **str** |  | [optional] [default to 'best_first']
**keywords_for_best_first** | **List[str]** |  | [optional] [default to []]
**keywords_weight** | **float** |  | [optional] [default to 0.5]

## Example

```python
from odin_sdk.models.crawl_config_update import CrawlConfigUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlConfigUpdate from a JSON string
crawl_config_update_instance = CrawlConfigUpdate.from_json(json)
# print the JSON string representation of the object
print(CrawlConfigUpdate.to_json())

# convert the object into a dict
crawl_config_update_dict = crawl_config_update_instance.to_dict()
# create an instance of CrawlConfigUpdate from a dict
crawl_config_update_from_dict = CrawlConfigUpdate.from_dict(crawl_config_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


