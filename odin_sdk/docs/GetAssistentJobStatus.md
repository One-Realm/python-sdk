# GetAssistentJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_list** | [**List[JobStatus]**](JobStatus.md) | List of job status objects. | 

## Example

```python
from odin_sdk.models.get_assistent_job_status import GetAssistentJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssistentJobStatus from a JSON string
get_assistent_job_status_instance = GetAssistentJobStatus.from_json(json)
# print the JSON string representation of the object
print(GetAssistentJobStatus.to_json())

# convert the object into a dict
get_assistent_job_status_dict = get_assistent_job_status_instance.to_dict()
# create an instance of GetAssistentJobStatus from a dict
get_assistent_job_status_from_dict = GetAssistentJobStatus.from_dict(get_assistent_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


