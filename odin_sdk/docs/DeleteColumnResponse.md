# DeleteColumnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**column_name** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_column_response import DeleteColumnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteColumnResponse from a JSON string
delete_column_response_instance = DeleteColumnResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteColumnResponse.to_json())

# convert the object into a dict
delete_column_response_dict = delete_column_response_instance.to_dict()
# create an instance of DeleteColumnResponse from a dict
delete_column_response_from_dict = DeleteColumnResponse.from_dict(delete_column_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


