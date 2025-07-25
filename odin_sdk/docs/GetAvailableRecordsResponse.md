# GetAvailableRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_view** | **List[object]** |  | 
**data_schema** | [**List[DTField]**](DTField.md) |  | 

## Example

```python
from odin_sdk.models.get_available_records_response import GetAvailableRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableRecordsResponse from a JSON string
get_available_records_response_instance = GetAvailableRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableRecordsResponse.to_json())

# convert the object into a dict
get_available_records_response_dict = get_available_records_response_instance.to_dict()
# create an instance of GetAvailableRecordsResponse from a dict
get_available_records_response_from_dict = GetAvailableRecordsResponse.from_dict(get_available_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


