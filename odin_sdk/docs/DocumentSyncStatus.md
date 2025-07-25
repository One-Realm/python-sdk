# DocumentSyncStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.document_sync_status import DocumentSyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSyncStatus from a JSON string
document_sync_status_instance = DocumentSyncStatus.from_json(json)
# print the JSON string representation of the object
print(DocumentSyncStatus.to_json())

# convert the object into a dict
document_sync_status_dict = document_sync_status_instance.to_dict()
# create an instance of DocumentSyncStatus from a dict
document_sync_status_from_dict = DocumentSyncStatus.from_dict(document_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


