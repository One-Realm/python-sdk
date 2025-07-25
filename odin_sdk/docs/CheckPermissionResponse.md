# CheckPermissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_permission** | **bool** |  | 
**permission** | **str** |  | 
**user_role** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.check_permission_response import CheckPermissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPermissionResponse from a JSON string
check_permission_response_instance = CheckPermissionResponse.from_json(json)
# print the JSON string representation of the object
print(CheckPermissionResponse.to_json())

# convert the object into a dict
check_permission_response_dict = check_permission_response_instance.to_dict()
# create an instance of CheckPermissionResponse from a dict
check_permission_response_from_dict = CheckPermissionResponse.from_dict(check_permission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


