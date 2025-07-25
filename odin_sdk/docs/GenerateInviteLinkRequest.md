# GenerateInviteLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**origin_url** | **str** |  | 
**role_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.generate_invite_link_request import GenerateInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateInviteLinkRequest from a JSON string
generate_invite_link_request_instance = GenerateInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateInviteLinkRequest.to_json())

# convert the object into a dict
generate_invite_link_request_dict = generate_invite_link_request_instance.to_dict()
# create an instance of GenerateInviteLinkRequest from a dict
generate_invite_link_request_from_dict = GenerateInviteLinkRequest.from_dict(generate_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


