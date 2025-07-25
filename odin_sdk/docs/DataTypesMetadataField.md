# DataTypesMetadataField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the metadata field | 
**datatype** | **str** | The data type of the metadata field | 
**description** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.data_types_metadata_field import DataTypesMetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypesMetadataField from a JSON string
data_types_metadata_field_instance = DataTypesMetadataField.from_json(json)
# print the JSON string representation of the object
print(DataTypesMetadataField.to_json())

# convert the object into a dict
data_types_metadata_field_dict = data_types_metadata_field_instance.to_dict()
# create an instance of DataTypesMetadataField from a dict
data_types_metadata_field_from_dict = DataTypesMetadataField.from_dict(data_types_metadata_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


