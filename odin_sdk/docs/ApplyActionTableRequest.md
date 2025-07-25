# ApplyActionTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | 
**data_type_id** | **str** | The data type ID of the table | 
**column_name** | **str** | The column containing the action configuration | 

## Example

```python
from odin_sdk.models.apply_action_table_request import ApplyActionTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyActionTableRequest from a JSON string
apply_action_table_request_instance = ApplyActionTableRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyActionTableRequest.to_json())

# convert the object into a dict
apply_action_table_request_dict = apply_action_table_request_instance.to_dict()
# create an instance of ApplyActionTableRequest from a dict
apply_action_table_request_from_dict = ApplyActionTableRequest.from_dict(apply_action_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


