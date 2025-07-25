# CreateSQLConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **str** | Type of the SQL connection. E.g. mysql, bigquery, generic, snowflake. | 
**project_id** | **str** | ID of the project to create the SQL connection. | 
**config** | [**Config**](Config.md) |  | 
**label** | **str** | Label for the SQL connection. E.g. &#39;Production DB&#39;. | 
**id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_sql_connection_request import CreateSQLConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSQLConnectionRequest from a JSON string
create_sql_connection_request_instance = CreateSQLConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSQLConnectionRequest.to_json())

# convert the object into a dict
create_sql_connection_request_dict = create_sql_connection_request_instance.to_dict()
# create an instance of CreateSQLConnectionRequest from a dict
create_sql_connection_request_from_dict = CreateSQLConnectionRequest.from_dict(create_sql_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


