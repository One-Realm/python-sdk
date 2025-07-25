# JobSubmissionResponse

Response model for job submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier for the submitted job | 
**status** | **str** | Initial status of the job | 
**message** | **str** | Descriptive message about job submission | 

## Example

```python
from odin_sdk.models.job_submission_response import JobSubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobSubmissionResponse from a JSON string
job_submission_response_instance = JobSubmissionResponse.from_json(json)
# print the JSON string representation of the object
print(JobSubmissionResponse.to_json())

# convert the object into a dict
job_submission_response_dict = job_submission_response_instance.to_dict()
# create an instance of JobSubmissionResponse from a dict
job_submission_response_from_dict = JobSubmissionResponse.from_dict(job_submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


