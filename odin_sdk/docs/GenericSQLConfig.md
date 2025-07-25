# GenericSQLConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectstring** | **str** | Connection string for the SQL database. | 
**tables** | **List[str]** | List of tables to be used in the SQL database. | 

## Example

```python
from odin_sdk.models.generic_sql_config import GenericSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenericSQLConfig from a JSON string
generic_sql_config_instance = GenericSQLConfig.from_json(json)
# print the JSON string representation of the object
print(GenericSQLConfig.to_json())

# convert the object into a dict
generic_sql_config_dict = generic_sql_config_instance.to_dict()
# create an instance of GenericSQLConfig from a dict
generic_sql_config_from_dict = GenericSQLConfig.from_dict(generic_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


