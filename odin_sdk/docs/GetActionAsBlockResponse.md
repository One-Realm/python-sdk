# GetActionAsBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[object]** | The list of actions as formatted agent blocks. | [optional] [default to []]

## Example

```python
from odin_sdk.models.get_action_as_block_response import GetActionAsBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionAsBlockResponse from a JSON string
get_action_as_block_response_instance = GetActionAsBlockResponse.from_json(json)
# print the JSON string representation of the object
print(GetActionAsBlockResponse.to_json())

# convert the object into a dict
get_action_as_block_response_dict = get_action_as_block_response_instance.to_dict()
# create an instance of GetActionAsBlockResponse from a dict
get_action_as_block_response_from_dict = GetActionAsBlockResponse.from_dict(get_action_as_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


