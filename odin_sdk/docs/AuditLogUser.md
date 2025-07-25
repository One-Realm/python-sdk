# AuditLogUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**profile_picture** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.audit_log_user import AuditLogUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogUser from a JSON string
audit_log_user_instance = AuditLogUser.from_json(json)
# print the JSON string representation of the object
print(AuditLogUser.to_json())

# convert the object into a dict
audit_log_user_dict = audit_log_user_instance.to_dict()
# create an instance of AuditLogUser from a dict
audit_log_user_from_dict = AuditLogUser.from_dict(audit_log_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


