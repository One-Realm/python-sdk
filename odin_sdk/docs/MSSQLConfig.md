# MSSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for the MS-SQL database. | 
**password** | **str** | Password for the MS-SQL database. | 
**host** | **str** | Host for the MS-SQL database. | 
**port** | **int** | Port for the MS-SQL database. | 
**database** | **str** | Database name for the MS-SQL database. | 
**tables** | **List[str]** | List of tables to be used in the MS-SQL database. | 
**always_trust_server** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.mssql_config import MSSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLConfig from a JSON string
mssql_config_instance = MSSQLConfig.from_json(json)
# print the JSON string representation of the object
print(MSSQLConfig.to_json())

# convert the object into a dict
mssql_config_dict = mssql_config_instance.to_dict()
# create an instance of MSSQLConfig from a dict
mssql_config_from_dict = MSSQLConfig.from_dict(mssql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


