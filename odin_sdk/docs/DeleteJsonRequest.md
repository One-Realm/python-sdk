# DeleteJsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**json_id** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_json_request import DeleteJsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteJsonRequest from a JSON string
delete_json_request_instance = DeleteJsonRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteJsonRequest.to_json())

# convert the object into a dict
delete_json_request_dict = delete_json_request_instance.to_dict()
# create an instance of DeleteJsonRequest from a dict
delete_json_request_from_dict = DeleteJsonRequest.from_dict(delete_json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


