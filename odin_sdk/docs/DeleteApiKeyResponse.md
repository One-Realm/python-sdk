# DeleteApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**detail** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_api_key_response import DeleteApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApiKeyResponse from a JSON string
delete_api_key_response_instance = DeleteApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteApiKeyResponse.to_json())

# convert the object into a dict
delete_api_key_response_dict = delete_api_key_response_instance.to_dict()
# create an instance of DeleteApiKeyResponse from a dict
delete_api_key_response_from_dict = DeleteApiKeyResponse.from_dict(delete_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


