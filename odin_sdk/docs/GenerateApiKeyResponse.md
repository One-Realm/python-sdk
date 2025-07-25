# GenerateApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**secret** | **str** |  | 

## Example

```python
from odin_sdk.models.generate_api_key_response import GenerateApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateApiKeyResponse from a JSON string
generate_api_key_response_instance = GenerateApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateApiKeyResponse.to_json())

# convert the object into a dict
generate_api_key_response_dict = generate_api_key_response_instance.to_dict()
# create an instance of GenerateApiKeyResponse from a dict
generate_api_key_response_from_dict = GenerateApiKeyResponse.from_dict(generate_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


