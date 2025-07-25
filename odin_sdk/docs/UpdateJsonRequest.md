# UpdateJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_id** | **str** |  | 
**data** | [**ModelJson**](ModelJson.md) |  | 

## Example

```python
from odin_sdk.models.update_json_request import UpdateJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateJsonRequest from a JSON string
update_json_request_instance = UpdateJsonRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateJsonRequest.to_json())

# convert the object into a dict
update_json_request_dict = update_json_request_instance.to_dict()
# create an instance of UpdateJsonRequest from a dict
update_json_request_from_dict = UpdateJsonRequest.from_dict(update_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


