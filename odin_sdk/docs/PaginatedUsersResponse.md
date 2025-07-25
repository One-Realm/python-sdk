# PaginatedUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**users** | [**List[UserResponse]**](UserResponse.md) |  | 

## Example

```python
from odin_sdk.models.paginated_users_response import PaginatedUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUsersResponse from a JSON string
paginated_users_response_instance = PaginatedUsersResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedUsersResponse.to_json())

# convert the object into a dict
paginated_users_response_dict = paginated_users_response_instance.to_dict()
# create an instance of PaginatedUsersResponse from a dict
paginated_users_response_from_dict = PaginatedUsersResponse.from_dict(paginated_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


