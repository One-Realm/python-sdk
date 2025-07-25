# UpdateColumnMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**options** | **object** |  | [optional] 
**not_null** | **bool** |  | [optional] 
**unique** | **bool** |  | [optional] 
**default_value** | [**AnyOf**](AnyOf.md) | Default value for the column | [optional] 

## Example

```python
from odin_sdk.models.update_column_metadata_request import UpdateColumnMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumnMetadataRequest from a JSON string
update_column_metadata_request_instance = UpdateColumnMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateColumnMetadataRequest.to_json())

# convert the object into a dict
update_column_metadata_request_dict = update_column_metadata_request_instance.to_dict()
# create an instance of UpdateColumnMetadataRequest from a dict
update_column_metadata_request_from_dict = UpdateColumnMetadataRequest.from_dict(update_column_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


