# QueuedKBFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[QueuedKBFileItem]**](QueuedKBFileItem.md) |  | 
**total** | **int** |  | 

## Example

```python
from odin_sdk.models.queued_kb_file_response import QueuedKBFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueuedKBFileResponse from a JSON string
queued_kb_file_response_instance = QueuedKBFileResponse.from_json(json)
# print the JSON string representation of the object
print(QueuedKBFileResponse.to_json())

# convert the object into a dict
queued_kb_file_response_dict = queued_kb_file_response_instance.to_dict()
# create an instance of QueuedKBFileResponse from a dict
queued_kb_file_response_from_dict = QueuedKBFileResponse.from_dict(queued_kb_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


