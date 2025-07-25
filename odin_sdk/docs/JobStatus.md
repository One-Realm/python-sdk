# JobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_type** | **str** | Type of job. | 
**uid** | **str** | User ID of the user who created the job. | 
**document_keys** | **List[str]** | List of document keys used in the job. | 
**job_id** | [**JobId**](JobId.md) |  | 
**use_job_id_path** | **bool** | Whether to use the job ID path for storage. Set automatically by the system. | 
**job_name** | **str** | Name of the job output. | 
**last_updated** | **float** | Timestamp of the last update to the job, in seconds. | 
**job_status** | **str** | Status of the job. | 
**project_id** | **str** | Project ID of the project the job belongs to. | 
**result_type** | **str** | File extension of the job output. | 
**credits_used** | **int** |  | [optional] 
**extra_info** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print(JobStatus.to_json())

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_from_dict = JobStatus.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


