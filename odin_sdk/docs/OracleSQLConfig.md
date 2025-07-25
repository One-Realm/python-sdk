# OracleSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for the OracleSQL database. | 
**password** | **str** | Password for the OracleSQL database. | 
**host** | **str** | Host for the OracleSQL database. | 
**port** | **int** | Port for the OracleSQL database. | 
**database** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**tables** | **List[str]** | List of tables to be used in the OracleSQL database. | 
**var_schema** | **str** | Schema for the OracleSQL database. | 

## Example

```python
from odin_sdk.models.oracle_sql_config import OracleSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OracleSQLConfig from a JSON string
oracle_sql_config_instance = OracleSQLConfig.from_json(json)
# print the JSON string representation of the object
print(OracleSQLConfig.to_json())

# convert the object into a dict
oracle_sql_config_dict = oracle_sql_config_instance.to_dict()
# create an instance of OracleSQLConfig from a dict
oracle_sql_config_from_dict = OracleSQLConfig.from_dict(oracle_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


