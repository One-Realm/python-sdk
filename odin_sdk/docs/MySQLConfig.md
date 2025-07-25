# MySQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for the MySQL database. | 
**password** | **str** | Password for the MySQL database. | 
**host** | **str** | Host for the MySQL database. | 
**port** | **int** | Port for the MySQL database. | 
**database** | **str** | Database name for the MySQL database. | 
**tables** | **List[str]** | List of tables to be used in the MySQL database. | 

## Example

```python
from odin_sdk.models.my_sql_config import MySQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MySQLConfig from a JSON string
my_sql_config_instance = MySQLConfig.from_json(json)
# print the JSON string representation of the object
print(MySQLConfig.to_json())

# convert the object into a dict
my_sql_config_dict = my_sql_config_instance.to_dict()
# create an instance of MySQLConfig from a dict
my_sql_config_from_dict = MySQLConfig.from_dict(my_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


