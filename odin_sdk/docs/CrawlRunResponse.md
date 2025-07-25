# CrawlRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**crawl_config_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**status** | **str** |  | 
**error_message** | **str** |  | 
**error_traceback** | **str** |  | 
**error_occurred** | **bool** |  | 
**error_occurred_at** | **datetime** |  | 

## Example

```python
from odin_sdk.models.crawl_run_response import CrawlRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlRunResponse from a JSON string
crawl_run_response_instance = CrawlRunResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlRunResponse.to_json())

# convert the object into a dict
crawl_run_response_dict = crawl_run_response_instance.to_dict()
# create an instance of CrawlRunResponse from a dict
crawl_run_response_from_dict = CrawlRunResponse.from_dict(crawl_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


