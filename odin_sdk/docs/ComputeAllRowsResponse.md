# ComputeAllRowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**total_rows_processed** | **int** |  | 
**total_columns_updated** | **int** |  | 
**updated_columns** | **List[str]** |  | 
**failed_rows** | **List[int]** |  | 
**stopped_due_to_failures** | **bool** |  | 
**retry_attempts** | **Dict[str, int]** |  | 
**computation_id** | **str** |  | [optional] 
**history_table** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.compute_all_rows_response import ComputeAllRowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeAllRowsResponse from a JSON string
compute_all_rows_response_instance = ComputeAllRowsResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeAllRowsResponse.to_json())

# convert the object into a dict
compute_all_rows_response_dict = compute_all_rows_response_instance.to_dict()
# create an instance of ComputeAllRowsResponse from a dict
compute_all_rows_response_from_dict = ComputeAllRowsResponse.from_dict(compute_all_rows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


