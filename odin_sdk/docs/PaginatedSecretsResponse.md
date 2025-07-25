# PaginatedSecretsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[SecretResponse]**](SecretResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from odin_sdk.models.paginated_secrets_response import PaginatedSecretsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSecretsResponse from a JSON string
paginated_secrets_response_instance = PaginatedSecretsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedSecretsResponse.to_json())

# convert the object into a dict
paginated_secrets_response_dict = paginated_secrets_response_instance.to_dict()
# create an instance of PaginatedSecretsResponse from a dict
paginated_secrets_response_from_dict = PaginatedSecretsResponse.from_dict(paginated_secrets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


