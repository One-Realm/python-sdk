# UpdateColumnMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**column_name** | **str** |  | 

## Example

```python
from odin_sdk.models.update_column_metadata_response import UpdateColumnMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumnMetadataResponse from a JSON string
update_column_metadata_response_instance = UpdateColumnMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateColumnMetadataResponse.to_json())

# convert the object into a dict
update_column_metadata_response_dict = update_column_metadata_response_instance.to_dict()
# create an instance of UpdateColumnMetadataResponse from a dict
update_column_metadata_response_from_dict = UpdateColumnMetadataResponse.from_dict(update_column_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


