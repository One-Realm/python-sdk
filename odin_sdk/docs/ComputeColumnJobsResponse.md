# ComputeColumnJobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**jobs** | **List[object]** |  | 
**total_count** | **int** |  | 

## Example

```python
from odin_sdk.models.compute_column_jobs_response import ComputeColumnJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnJobsResponse from a JSON string
compute_column_jobs_response_instance = ComputeColumnJobsResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeColumnJobsResponse.to_json())

# convert the object into a dict
compute_column_jobs_response_dict = compute_column_jobs_response_instance.to_dict()
# create an instance of ComputeColumnJobsResponse from a dict
compute_column_jobs_response_from_dict = ComputeColumnJobsResponse.from_dict(compute_column_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


