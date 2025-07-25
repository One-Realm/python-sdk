# MembersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[RoutesUsersMember]**](RoutesUsersMember.md) |  | 
**invitations** | [**List[Invitation]**](Invitation.md) |  | 

## Example

```python
from odin_sdk.models.members_response import MembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembersResponse from a JSON string
members_response_instance = MembersResponse.from_json(json)
# print the JSON string representation of the object
print(MembersResponse.to_json())

# convert the object into a dict
members_response_dict = members_response_instance.to_dict()
# create an instance of MembersResponse from a dict
members_response_from_dict = MembersResponse.from_dict(members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


