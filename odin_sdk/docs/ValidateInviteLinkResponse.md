# ValidateInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | 
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**project_description** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.validate_invite_link_response import ValidateInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateInviteLinkResponse from a JSON string
validate_invite_link_response_instance = ValidateInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateInviteLinkResponse.to_json())

# convert the object into a dict
validate_invite_link_response_dict = validate_invite_link_response_instance.to_dict()
# create an instance of ValidateInviteLinkResponse from a dict
validate_invite_link_response_from_dict = ValidateInviteLinkResponse.from_dict(validate_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


