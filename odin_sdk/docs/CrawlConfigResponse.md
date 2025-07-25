# CrawlConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**crawl_name** | **str** |  | 
**root_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**project_id** | **str** |  | 
**user_id** | **str** |  | 
**repeat** | **float** |  | 
**limit_to_root_domain** | **bool** |  | 
**limit_to_domains** | **List[str]** |  | 
**limit_to_patterns** | **List[str]** |  | 
**download_files** | **bool** |  | 
**max_depth** | **int** |  | 
**max_pages** | **int** |  | 
**strategy** | **str** |  | 
**keywords_for_best_first** | **List[str]** |  | 
**keywords_weight** | **float** |  | 

## Example

```python
from odin_sdk.models.crawl_config_response import CrawlConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlConfigResponse from a JSON string
crawl_config_response_instance = CrawlConfigResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlConfigResponse.to_json())

# convert the object into a dict
crawl_config_response_dict = crawl_config_response_instance.to_dict()
# create an instance of CrawlConfigResponse from a dict
crawl_config_response_from_dict = CrawlConfigResponse.from_dict(crawl_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


