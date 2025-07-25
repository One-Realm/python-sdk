# ExtractDataTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **str** | The ID of the data type to set for the documents. | 
**document_ids** | **List[str]** | The list of document keys to set the data type for. | 
**data_table_row_id** | [**DataTableRowId**](DataTableRowId.md) |  | [optional] 

## Example

```python
from odin_sdk.models.extract_data_type_request import ExtractDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractDataTypeRequest from a JSON string
extract_data_type_request_instance = ExtractDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print(ExtractDataTypeRequest.to_json())

# convert the object into a dict
extract_data_type_request_dict = extract_data_type_request_instance.to_dict()
# create an instance of ExtractDataTypeRequest from a dict
extract_data_type_request_from_dict = ExtractDataTypeRequest.from_dict(extract_data_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


