# GetGroupedDataTypeViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**grouped_data** | **List[object]** |  | 
**data_schema** | [**List[DTField]**](DTField.md) |  | 
**views** | **List[object]** |  | 
**total_count** | **int** |  | 
**group_config** | **object** |  | 

## Example

```python
from odin_sdk.models.get_grouped_data_type_view_response import GetGroupedDataTypeViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupedDataTypeViewResponse from a JSON string
get_grouped_data_type_view_response_instance = GetGroupedDataTypeViewResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupedDataTypeViewResponse.to_json())

# convert the object into a dict
get_grouped_data_type_view_response_dict = get_grouped_data_type_view_response_instance.to_dict()
# create an instance of GetGroupedDataTypeViewResponse from a dict
get_grouped_data_type_view_response_from_dict = GetGroupedDataTypeViewResponse.from_dict(get_grouped_data_type_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


