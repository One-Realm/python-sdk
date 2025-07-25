# SaveContextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**context** | **str** |  | 

## Example

```python
from odin_sdk.models.save_context_request import SaveContextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveContextRequest from a JSON string
save_context_request_instance = SaveContextRequest.from_json(json)
# print the JSON string representation of the object
print(SaveContextRequest.to_json())

# convert the object into a dict
save_context_request_dict = save_context_request_instance.to_dict()
# create an instance of SaveContextRequest from a dict
save_context_request_from_dict = SaveContextRequest.from_dict(save_context_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


