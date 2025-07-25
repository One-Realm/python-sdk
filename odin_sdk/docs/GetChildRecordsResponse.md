# GetChildRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_view** | **List[object]** |  | 
**data_schema** | [**List[DTField]**](DTField.md) |  | 
**parent_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_child_records_response import GetChildRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChildRecordsResponse from a JSON string
get_child_records_response_instance = GetChildRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(GetChildRecordsResponse.to_json())

# convert the object into a dict
get_child_records_response_dict = get_child_records_response_instance.to_dict()
# create an instance of GetChildRecordsResponse from a dict
get_child_records_response_from_dict = GetChildRecordsResponse.from_dict(get_child_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


