# GetDataTypeJsonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_json** | **object** |  | 

## Example

```python
from odin_sdk.models.get_data_type_json_response import GetDataTypeJsonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataTypeJsonResponse from a JSON string
get_data_type_json_response_instance = GetDataTypeJsonResponse.from_json(json)
# print the JSON string representation of the object
print(GetDataTypeJsonResponse.to_json())

# convert the object into a dict
get_data_type_json_response_dict = get_data_type_json_response_instance.to_dict()
# create an instance of GetDataTypeJsonResponse from a dict
get_data_type_json_response_from_dict = GetDataTypeJsonResponse.from_dict(get_data_type_json_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


