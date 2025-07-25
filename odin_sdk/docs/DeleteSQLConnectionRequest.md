# DeleteSQLConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the SQL connection to delete. | 
**project_id** | **str** | ID of the project in which to delete the SQL connection. Must be provided to authorize the action. | 

## Example

```python
from odin_sdk.models.delete_sql_connection_request import DeleteSQLConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSQLConnectionRequest from a JSON string
delete_sql_connection_request_instance = DeleteSQLConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSQLConnectionRequest.to_json())

# convert the object into a dict
delete_sql_connection_request_dict = delete_sql_connection_request_instance.to_dict()
# create an instance of DeleteSQLConnectionRequest from a dict
delete_sql_connection_request_from_dict = DeleteSQLConnectionRequest.from_dict(delete_sql_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


