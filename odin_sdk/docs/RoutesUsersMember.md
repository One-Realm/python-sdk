# RoutesUsersMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**uid** | **str** |  | 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**is_pending** | **bool** |  | [optional] 
**credit_limit** | **int** |  | [optional] 
**credit_limit_override** | **bool** |  | [optional] 
**credits_used** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.routes_users_member import RoutesUsersMember

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesUsersMember from a JSON string
routes_users_member_instance = RoutesUsersMember.from_json(json)
# print the JSON string representation of the object
print(RoutesUsersMember.to_json())

# convert the object into a dict
routes_users_member_dict = routes_users_member_instance.to_dict()
# create an instance of RoutesUsersMember from a dict
routes_users_member_from_dict = RoutesUsersMember.from_dict(routes_users_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


