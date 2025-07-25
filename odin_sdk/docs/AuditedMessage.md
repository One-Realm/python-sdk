# AuditedMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_message** | **str** |  | 
**masked_message** | **str** |  | 
**response** | **str** |  | 

## Example

```python
from odin_sdk.models.audited_message import AuditedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditedMessage from a JSON string
audited_message_instance = AuditedMessage.from_json(json)
# print the JSON string representation of the object
print(AuditedMessage.to_json())

# convert the object into a dict
audited_message_dict = audited_message_instance.to_dict()
# create an instance of AuditedMessage from a dict
audited_message_from_dict = AuditedMessage.from_dict(audited_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


