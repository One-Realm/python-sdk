# UpdateColumnValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | The name of the column to update | 
**new_value** | **object** |  | 

## Example

```python
from odin_sdk.models.update_column_value_request import UpdateColumnValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumnValueRequest from a JSON string
update_column_value_request_instance = UpdateColumnValueRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateColumnValueRequest.to_json())

# convert the object into a dict
update_column_value_request_dict = update_column_value_request_instance.to_dict()
# create an instance of UpdateColumnValueRequest from a dict
update_column_value_request_from_dict = UpdateColumnValueRequest.from_dict(update_column_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


