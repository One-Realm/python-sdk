# MessageGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_messages** | **int** |  | 
**messages** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.message_group import MessageGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MessageGroup from a JSON string
message_group_instance = MessageGroup.from_json(json)
# print the JSON string representation of the object
print(MessageGroup.to_json())

# convert the object into a dict
message_group_dict = message_group_instance.to_dict()
# create an instance of MessageGroup from a dict
message_group_from_dict = MessageGroup.from_dict(message_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


