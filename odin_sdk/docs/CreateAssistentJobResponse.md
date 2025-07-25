# CreateAssistentJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | ID of the created job. | 
**job_status** | **str** | Status of the created job. | 
**job_type** | **str** | Type of the created job. | 

## Example

```python
from odin_sdk.models.create_assistent_job_response import CreateAssistentJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssistentJobResponse from a JSON string
create_assistent_job_response_instance = CreateAssistentJobResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAssistentJobResponse.to_json())

# convert the object into a dict
create_assistent_job_response_dict = create_assistent_job_response_instance.to_dict()
# create an instance of CreateAssistentJobResponse from a dict
create_assistent_job_response_from_dict = CreateAssistentJobResponse.from_dict(create_assistent_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


