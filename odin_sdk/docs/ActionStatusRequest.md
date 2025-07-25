# ActionStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | 
**data_type_id** | **str** | The data type ID of the table | 
**row_id** | [**RowId**](RowId.md) |  | 
**column_name** | **str** | The column name containing the action configuration | 
**flow_run_id** | **str** | The flow run ID to check status for | 

## Example

```python
from odin_sdk.models.action_status_request import ActionStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionStatusRequest from a JSON string
action_status_request_instance = ActionStatusRequest.from_json(json)
# print the JSON string representation of the object
print(ActionStatusRequest.to_json())

# convert the object into a dict
action_status_request_dict = action_status_request_instance.to_dict()
# create an instance of ActionStatusRequest from a dict
action_status_request_from_dict = ActionStatusRequest.from_dict(action_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


