# CrawlResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **str** |  | 
**crawl_id** | **str** |  | 
**run_id** | **str** |  | 
**url** | **str** |  | 
**content** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from odin_sdk.models.crawl_result_response import CrawlResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlResultResponse from a JSON string
crawl_result_response_instance = CrawlResultResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlResultResponse.to_json())

# convert the object into a dict
crawl_result_response_dict = crawl_result_response_instance.to_dict()
# create an instance of CrawlResultResponse from a dict
crawl_result_response_from_dict = CrawlResultResponse.from_dict(crawl_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


