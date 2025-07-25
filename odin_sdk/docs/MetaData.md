# MetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**added_by** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**char_count** | **int** |  | [optional] 
**disk_usage** | **int** |  | [optional] 
**custom_metadata** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.meta_data import MetaData

# TODO update the JSON string below
json = "{}"
# create an instance of MetaData from a JSON string
meta_data_instance = MetaData.from_json(json)
# print the JSON string representation of the object
print(MetaData.to_json())

# convert the object into a dict
meta_data_dict = meta_data_instance.to_dict()
# create an instance of MetaData from a dict
meta_data_from_dict = MetaData.from_dict(meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


