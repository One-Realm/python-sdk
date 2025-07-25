# SyncKBRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entire_kb** | **bool** |  | [optional] 
**project_id** | **str** |  | 
**docs** | [**List[FileData]**](FileData.md) |  | [optional] 

## Example

```python
from odin_sdk.models.sync_kb_request import SyncKBRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncKBRequest from a JSON string
sync_kb_request_instance = SyncKBRequest.from_json(json)
# print the JSON string representation of the object
print(SyncKBRequest.to_json())

# convert the object into a dict
sync_kb_request_dict = sync_kb_request_instance.to_dict()
# create an instance of SyncKBRequest from a dict
sync_kb_request_from_dict = SyncKBRequest.from_dict(sync_kb_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


