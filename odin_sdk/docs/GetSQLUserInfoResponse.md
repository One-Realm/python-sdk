# GetSQLUserInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**sql_user_info** | **object** |  | 

## Example

```python
from odin_sdk.models.get_sql_user_info_response import GetSQLUserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSQLUserInfoResponse from a JSON string
get_sql_user_info_response_instance = GetSQLUserInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSQLUserInfoResponse.to_json())

# convert the object into a dict
get_sql_user_info_response_dict = get_sql_user_info_response_instance.to_dict()
# create an instance of GetSQLUserInfoResponse from a dict
get_sql_user_info_response_from_dict = GetSQLUserInfoResponse.from_dict(get_sql_user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


