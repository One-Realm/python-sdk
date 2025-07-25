# UpdateChatTestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.update_chat_test_data import UpdateChatTestData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatTestData from a JSON string
update_chat_test_data_instance = UpdateChatTestData.from_json(json)
# print the JSON string representation of the object
print(UpdateChatTestData.to_json())

# convert the object into a dict
update_chat_test_data_dict = update_chat_test_data_instance.to_dict()
# create an instance of UpdateChatTestData from a dict
update_chat_test_data_from_dict = UpdateChatTestData.from_dict(update_chat_test_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


