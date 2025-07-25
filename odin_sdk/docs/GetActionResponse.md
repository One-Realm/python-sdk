# GetActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[OdinActionModel]**](OdinActionModel.md) | The list of actions. | [optional] [default to []]

## Example

```python
from odin_sdk.models.get_action_response import GetActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionResponse from a JSON string
get_action_response_instance = GetActionResponse.from_json(json)
# print the JSON string representation of the object
print(GetActionResponse.to_json())

# convert the object into a dict
get_action_response_dict = get_action_response_instance.to_dict()
# create an instance of GetActionResponse from a dict
get_action_response_from_dict = GetActionResponse.from_dict(get_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


