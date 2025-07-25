# ExtractDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **str** | The Data Type ID | 
**data_type** | **object** |  | [optional] 
**data_type_extracted** | **List[object]** | The Metadata after extracting the data type | 
**data_type_name** | **str** | Name of data type | 

## Example

```python
from odin_sdk.models.extract_data_type_response import ExtractDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractDataTypeResponse from a JSON string
extract_data_type_response_instance = ExtractDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractDataTypeResponse.to_json())

# convert the object into a dict
extract_data_type_response_dict = extract_data_type_response_instance.to_dict()
# create an instance of ExtractDataTypeResponse from a dict
extract_data_type_response_from_dict = ExtractDataTypeResponse.from_dict(extract_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


