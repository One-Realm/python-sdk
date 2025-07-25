# UserTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.user_tag_request import UserTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserTagRequest from a JSON string
user_tag_request_instance = UserTagRequest.from_json(json)
# print the JSON string representation of the object
print(UserTagRequest.to_json())

# convert the object into a dict
user_tag_request_dict = user_tag_request_instance.to_dict()
# create an instance of UserTagRequest from a dict
user_tag_request_from_dict = UserTagRequest.from_dict(user_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


