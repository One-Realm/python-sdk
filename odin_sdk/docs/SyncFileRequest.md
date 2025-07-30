# SyncFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**project_id** | **str** |  | 
**metadata** | **object** |  | [optional] 
**resource_type_id** | **str** |  | [optional] 
**is_quick_upload** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.sync_file_request import SyncFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncFileRequest from a JSON string
sync_file_request_instance = SyncFileRequest.from_json(json)
# print the JSON string representation of the object
print(SyncFileRequest.to_json())

# convert the object into a dict
sync_file_request_dict = sync_file_request_instance.to_dict()
# create an instance of SyncFileRequest from a dict
sync_file_request_from_dict = SyncFileRequest.from_dict(sync_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


