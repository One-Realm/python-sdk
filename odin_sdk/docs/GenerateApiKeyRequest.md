# GenerateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** |  | [optional] [default to '']

## Example

```python
from odin_sdk.models.generate_api_key_request import GenerateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateApiKeyRequest from a JSON string
generate_api_key_request_instance = GenerateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateApiKeyRequest.to_json())

# convert the object into a dict
generate_api_key_request_dict = generate_api_key_request_instance.to_dict()
# create an instance of GenerateApiKeyRequest from a dict
generate_api_key_request_from_dict = GenerateApiKeyRequest.from_dict(generate_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


