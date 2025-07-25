# TestChat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.test_chat import TestChat

# TODO update the JSON string below
json = "{}"
# create an instance of TestChat from a JSON string
test_chat_instance = TestChat.from_json(json)
# print the JSON string representation of the object
print(TestChat.to_json())

# convert the object into a dict
test_chat_dict = test_chat_instance.to_dict()
# create an instance of TestChat from a dict
test_chat_from_dict = TestChat.from_dict(test_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


