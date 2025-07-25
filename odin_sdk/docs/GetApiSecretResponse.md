# GetApiSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_secret** | **str** |  | 

## Example

```python
from odin_sdk.models.get_api_secret_response import GetApiSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiSecretResponse from a JSON string
get_api_secret_response_instance = GetApiSecretResponse.from_json(json)
# print the JSON string representation of the object
print(GetApiSecretResponse.to_json())

# convert the object into a dict
get_api_secret_response_dict = get_api_secret_response_instance.to_dict()
# create an instance of GetApiSecretResponse from a dict
get_api_secret_response_from_dict = GetApiSecretResponse.from_dict(get_api_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


