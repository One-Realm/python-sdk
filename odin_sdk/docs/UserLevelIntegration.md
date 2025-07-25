# UserLevelIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**integration_id** | **str** |  | 
**integration_type** | **str** |  | 

## Example

```python
from odin_sdk.models.user_level_integration import UserLevelIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of UserLevelIntegration from a JSON string
user_level_integration_instance = UserLevelIntegration.from_json(json)
# print the JSON string representation of the object
print(UserLevelIntegration.to_json())

# convert the object into a dict
user_level_integration_dict = user_level_integration_instance.to_dict()
# create an instance of UserLevelIntegration from a dict
user_level_integration_from_dict = UserLevelIntegration.from_dict(user_level_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


