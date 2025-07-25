# GetJsonsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_jsons_request import GetJsonsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetJsonsRequest from a JSON string
get_jsons_request_instance = GetJsonsRequest.from_json(json)
# print the JSON string representation of the object
print(GetJsonsRequest.to_json())

# convert the object into a dict
get_jsons_request_dict = get_jsons_request_instance.to_dict()
# create an instance of GetJsonsRequest from a dict
get_jsons_request_from_dict = GetJsonsRequest.from_dict(get_jsons_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


