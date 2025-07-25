# UserNameChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.user_name_change_response import UserNameChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameChangeResponse from a JSON string
user_name_change_response_instance = UserNameChangeResponse.from_json(json)
# print the JSON string representation of the object
print(UserNameChangeResponse.to_json())

# convert the object into a dict
user_name_change_response_dict = user_name_change_response_instance.to_dict()
# create an instance of UserNameChangeResponse from a dict
user_name_change_response_from_dict = UserNameChangeResponse.from_dict(user_name_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


