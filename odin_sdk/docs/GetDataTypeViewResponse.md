# GetDataTypeViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_view** | **List[object]** |  | 
**data_schema** | [**List[DTField]**](DTField.md) |  | 
**views** | **List[object]** |  | 
**pagination** | **object** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.get_data_type_view_response import GetDataTypeViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataTypeViewResponse from a JSON string
get_data_type_view_response_instance = GetDataTypeViewResponse.from_json(json)
# print the JSON string representation of the object
print(GetDataTypeViewResponse.to_json())

# convert the object into a dict
get_data_type_view_response_dict = get_data_type_view_response_instance.to_dict()
# create an instance of GetDataTypeViewResponse from a dict
get_data_type_view_response_from_dict = GetDataTypeViewResponse.from_dict(get_data_type_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


