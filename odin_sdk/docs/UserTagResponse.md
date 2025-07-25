# UserTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.user_tag_response import UserTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTagResponse from a JSON string
user_tag_response_instance = UserTagResponse.from_json(json)
# print the JSON string representation of the object
print(UserTagResponse.to_json())

# convert the object into a dict
user_tag_response_dict = user_tag_response_instance.to_dict()
# create an instance of UserTagResponse from a dict
user_tag_response_from_dict = UserTagResponse.from_dict(user_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


