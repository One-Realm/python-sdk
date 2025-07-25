# GetAffectedChatsCountWhenEnablingRetentionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**retention_days** | **int** |  | 

## Example

```python
from odin_sdk.models.get_affected_chats_count_when_enabling_retention_request import GetAffectedChatsCountWhenEnablingRetentionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAffectedChatsCountWhenEnablingRetentionRequest from a JSON string
get_affected_chats_count_when_enabling_retention_request_instance = GetAffectedChatsCountWhenEnablingRetentionRequest.from_json(json)
# print the JSON string representation of the object
print(GetAffectedChatsCountWhenEnablingRetentionRequest.to_json())

# convert the object into a dict
get_affected_chats_count_when_enabling_retention_request_dict = get_affected_chats_count_when_enabling_retention_request_instance.to_dict()
# create an instance of GetAffectedChatsCountWhenEnablingRetentionRequest from a dict
get_affected_chats_count_when_enabling_retention_request_from_dict = GetAffectedChatsCountWhenEnablingRetentionRequest.from_dict(get_affected_chats_count_when_enabling_retention_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


