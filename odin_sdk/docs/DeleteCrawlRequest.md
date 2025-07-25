# DeleteCrawlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_crawl_request import DeleteCrawlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCrawlRequest from a JSON string
delete_crawl_request_instance = DeleteCrawlRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCrawlRequest.to_json())

# convert the object into a dict
delete_crawl_request_dict = delete_crawl_request_instance.to_dict()
# create an instance of DeleteCrawlRequest from a dict
delete_crawl_request_from_dict = DeleteCrawlRequest.from_dict(delete_crawl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


