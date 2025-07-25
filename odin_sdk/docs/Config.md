# Config

Configuration for the SQL connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for the OracleSQL database. | 
**password** | **str** | Password for the OracleSQL database. | 
**host** | **str** | Host for the OracleSQL database. | 
**port** | **int** | Port for the OracleSQL database. | 
**database** | **str** |  | 
**tables** | **List[str]** | List of tables to be used in the OracleSQL database. | 
**connectstring** | **str** | Connection string for the SQL database. | 
**always_trust_server** | **bool** |  | [optional] 
**account** | **str** | Account for the SnowflakeSQL database. | 
**var_schema** | **str** | Schema for the OracleSQL database. | 
**warehouse** | **str** | Warehouse for the SnowflakeSQL database. | 
**role** | **str** | Role for the SnowflakeSQL database. | 
**service_name** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print(Config.to_json())

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_from_dict = Config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


