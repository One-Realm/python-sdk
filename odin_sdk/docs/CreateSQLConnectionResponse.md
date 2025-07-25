# CreateSQLConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.create_sql_connection_response import CreateSQLConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSQLConnectionResponse from a JSON string
create_sql_connection_response_instance = CreateSQLConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSQLConnectionResponse.to_json())

# convert the object into a dict
create_sql_connection_response_dict = create_sql_connection_response_instance.to_dict()
# create an instance of CreateSQLConnectionResponse from a dict
create_sql_connection_response_from_dict = CreateSQLConnectionResponse.from_dict(create_sql_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


