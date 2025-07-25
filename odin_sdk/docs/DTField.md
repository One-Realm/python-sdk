# DTField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the field | 
**name** | **str** | Name of the field | 
**description** | **str** |  | [optional] 
**options** | **object** |  | [optional] 
**type** | **str** | Field type (e.g., text, number, etc.) | 
**cell_value_type** | **str** | Type of value stored in cells | 
**is_multiple_cell_value** | **bool** | Whether field can contain multiple values | [optional] [default to False]
**db_field_type** | **str** | Database field type | 
**db_field_name** | **str** | Name of the field in database | 
**not_null** | **bool** | Whether field is required | [optional] [default to False]
**unique** | **bool** | Whether field values must be unique | [optional] [default to False]
**is_primary** | **bool** | Whether field is primary key | [optional] [default to False]
**is_computed** | **bool** | Whether field is computed | [optional] [default to False]
**is_lookup** | **bool** | Whether field is a lookup field | [optional] [default to False]
**is_pending** | **bool** | Whether field is pending creation | [optional] [default to False]
**has_error** | **bool** | Whether field has errors | [optional] [default to False]
**lookup_linked_field_id** | **str** |  | [optional] 
**lookup_options** | **str** |  | [optional] 
**table_id** | **str** | ID of the table this field belongs to | 
**version** | **int** | Version number of the field | [optional] [default to 1]
**created_time** | **datetime** | Creation timestamp | [optional] 
**last_modified_time** | **datetime** |  | [optional] 
**deleted_time** | **datetime** |  | [optional] 
**created_by** | **str** | User ID who created the field | 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.dt_field import DTField

# TODO update the JSON string below
json = "{}"
# create an instance of DTField from a JSON string
dt_field_instance = DTField.from_json(json)
# print the JSON string representation of the object
print(DTField.to_json())

# convert the object into a dict
dt_field_dict = dt_field_instance.to_dict()
# create an instance of DTField from a dict
dt_field_from_dict = DTField.from_dict(dt_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


