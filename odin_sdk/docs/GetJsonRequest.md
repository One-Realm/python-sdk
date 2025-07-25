# GetJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**json_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_json_request import GetJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetJsonRequest from a JSON string
get_json_request_instance = GetJsonRequest.from_json(json)
# print the JSON string representation of the object
print(GetJsonRequest.to_json())

# convert the object into a dict
get_json_request_dict = get_json_request_instance.to_dict()
# create an instance of GetJsonRequest from a dict
get_json_request_from_dict = GetJsonRequest.from_dict(get_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


