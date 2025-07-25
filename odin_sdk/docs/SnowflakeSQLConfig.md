# SnowflakeSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account for the SnowflakeSQL database. | 
**username** | **str** | Username for the SnowflakeSQL database. | 
**password** | **str** | Password for the SnowflakeSQL database. | 
**database** | **str** | Database for the SnowflakeSQL database. | 
**var_schema** | **str** | Schema for the SnowflakeSQL database. | 
**warehouse** | **str** | Warehouse for the SnowflakeSQL database. | 
**role** | **str** | Role for the SnowflakeSQL database. | 

## Example

```python
from odin_sdk.models.snowflake_sql_config import SnowflakeSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeSQLConfig from a JSON string
snowflake_sql_config_instance = SnowflakeSQLConfig.from_json(json)
# print the JSON string representation of the object
print(SnowflakeSQLConfig.to_json())

# convert the object into a dict
snowflake_sql_config_dict = snowflake_sql_config_instance.to_dict()
# create an instance of SnowflakeSQLConfig from a dict
snowflake_sql_config_from_dict = SnowflakeSQLConfig.from_dict(snowflake_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


