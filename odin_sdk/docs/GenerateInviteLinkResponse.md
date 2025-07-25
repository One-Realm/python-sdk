# GenerateInviteLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_link** | **str** |  | 
**invite_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.generate_invite_link_response import GenerateInviteLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateInviteLinkResponse from a JSON string
generate_invite_link_response_instance = GenerateInviteLinkResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateInviteLinkResponse.to_json())

# convert the object into a dict
generate_invite_link_response_dict = generate_invite_link_response_instance.to_dict()
# create an instance of GenerateInviteLinkResponse from a dict
generate_invite_link_response_from_dict = GenerateInviteLinkResponse.from_dict(generate_invite_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


