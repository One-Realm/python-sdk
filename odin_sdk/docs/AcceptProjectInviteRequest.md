# AcceptProjectInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 

## Example

```python
from odin_sdk.models.accept_project_invite_request import AcceptProjectInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptProjectInviteRequest from a JSON string
accept_project_invite_request_instance = AcceptProjectInviteRequest.from_json(json)
# print the JSON string representation of the object
print(AcceptProjectInviteRequest.to_json())

# convert the object into a dict
accept_project_invite_request_dict = accept_project_invite_request_instance.to_dict()
# create an instance of AcceptProjectInviteRequest from a dict
accept_project_invite_request_from_dict = AcceptProjectInviteRequest.from_dict(accept_project_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


