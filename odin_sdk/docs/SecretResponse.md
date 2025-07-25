# SecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**created_by** | **str** |  | 
**creator_email** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_deleted** | **bool** |  | [optional] 
**is_encrypted** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.secret_response import SecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretResponse from a JSON string
secret_response_instance = SecretResponse.from_json(json)
# print the JSON string representation of the object
print(SecretResponse.to_json())

# convert the object into a dict
secret_response_dict = secret_response_instance.to_dict()
# create an instance of SecretResponse from a dict
secret_response_from_dict = SecretResponse.from_dict(secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


