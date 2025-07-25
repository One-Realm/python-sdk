# UserNameChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from odin_sdk.models.user_name_change_request import UserNameChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameChangeRequest from a JSON string
user_name_change_request_instance = UserNameChangeRequest.from_json(json)
# print the JSON string representation of the object
print(UserNameChangeRequest.to_json())

# convert the object into a dict
user_name_change_request_dict = user_name_change_request_instance.to_dict()
# create an instance of UserNameChangeRequest from a dict
user_name_change_request_from_dict = UserNameChangeRequest.from_dict(user_name_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


