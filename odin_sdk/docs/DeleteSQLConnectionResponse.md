# DeleteSQLConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.delete_sql_connection_response import DeleteSQLConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSQLConnectionResponse from a JSON string
delete_sql_connection_response_instance = DeleteSQLConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSQLConnectionResponse.to_json())

# convert the object into a dict
delete_sql_connection_response_dict = delete_sql_connection_response_instance.to_dict()
# create an instance of DeleteSQLConnectionResponse from a dict
delete_sql_connection_response_from_dict = DeleteSQLConnectionResponse.from_dict(delete_sql_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


