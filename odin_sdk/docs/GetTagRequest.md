# GetTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_tag_request import GetTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagRequest from a JSON string
get_tag_request_instance = GetTagRequest.from_json(json)
# print the JSON string representation of the object
print(GetTagRequest.to_json())

# convert the object into a dict
get_tag_request_dict = get_tag_request_instance.to_dict()
# create an instance of GetTagRequest from a dict
get_tag_request_from_dict = GetTagRequest.from_dict(get_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


