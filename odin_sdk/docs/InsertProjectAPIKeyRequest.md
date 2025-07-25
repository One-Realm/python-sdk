# InsertProjectAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | **str** |  | 
**api_key** | **str** |  | 

## Example

```python
from odin_sdk.models.insert_project_api_key_request import InsertProjectAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertProjectAPIKeyRequest from a JSON string
insert_project_api_key_request_instance = InsertProjectAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(InsertProjectAPIKeyRequest.to_json())

# convert the object into a dict
insert_project_api_key_request_dict = insert_project_api_key_request_instance.to_dict()
# create an instance of InsertProjectAPIKeyRequest from a dict
insert_project_api_key_request_from_dict = InsertProjectAPIKeyRequest.from_dict(insert_project_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


