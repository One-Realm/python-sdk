# SelectUrlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**knowledge_base** | **object** |  | 

## Example

```python
from odin_sdk.models.select_urls_response import SelectUrlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelectUrlsResponse from a JSON string
select_urls_response_instance = SelectUrlsResponse.from_json(json)
# print the JSON string representation of the object
print(SelectUrlsResponse.to_json())

# convert the object into a dict
select_urls_response_dict = select_urls_response_instance.to_dict()
# create an instance of SelectUrlsResponse from a dict
select_urls_response_from_dict = SelectUrlsResponse.from_dict(select_urls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


