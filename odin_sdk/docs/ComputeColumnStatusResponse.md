# ComputeColumnStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**execution_id** | **str** |  | 
**status** | **str** |  | 
**progress_percentage** | **float** |  | 
**processed_rows** | **int** |  | 
**total_rows** | **int** |  | 
**updated_rows** | **int** |  | 
**failed_rows** | **List[int]** |  | 
**started_at** | **str** |  | 
**completed_at** | **str** |  | 
**error_message** | **str** |  | 
**metadata** | **object** |  | 

## Example

```python
from odin_sdk.models.compute_column_status_response import ComputeColumnStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnStatusResponse from a JSON string
compute_column_status_response_instance = ComputeColumnStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeColumnStatusResponse.to_json())

# convert the object into a dict
compute_column_status_response_dict = compute_column_status_response_instance.to_dict()
# create an instance of ComputeColumnStatusResponse from a dict
compute_column_status_response_from_dict = ComputeColumnStatusResponse.from_dict(compute_column_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


