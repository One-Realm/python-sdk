# UserProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**providers** | **List[str]** |  | [optional] 

## Example

```python
from odin_sdk.models.user_providers_response import UserProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProvidersResponse from a JSON string
user_providers_response_instance = UserProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(UserProvidersResponse.to_json())

# convert the object into a dict
user_providers_response_dict = user_providers_response_instance.to_dict()
# create an instance of UserProvidersResponse from a dict
user_providers_response_from_dict = UserProvidersResponse.from_dict(user_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


