# SelectUrlsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**document_key** | **str** |  | 
**knowledge_base** | **object** |  | 

## Example

```python
from odin_sdk.models.select_urls_request import SelectUrlsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelectUrlsRequest from a JSON string
select_urls_request_instance = SelectUrlsRequest.from_json(json)
# print the JSON string representation of the object
print(SelectUrlsRequest.to_json())

# convert the object into a dict
select_urls_request_dict = select_urls_request_instance.to_dict()
# create an instance of SelectUrlsRequest from a dict
select_urls_request_from_dict = SelectUrlsRequest.from_dict(select_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


