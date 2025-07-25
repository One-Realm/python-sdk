# DeleteActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | The message of the response. | 

## Example

```python
from odin_sdk.models.delete_action_response import DeleteActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteActionResponse from a JSON string
delete_action_response_instance = DeleteActionResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteActionResponse.to_json())

# convert the object into a dict
delete_action_response_dict = delete_action_response_instance.to_dict()
# create an instance of DeleteActionResponse from a dict
delete_action_response_from_dict = DeleteActionResponse.from_dict(delete_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


