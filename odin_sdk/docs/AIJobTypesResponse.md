# AIJobTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_info** | **object** | Information about the job types. | [optional] 

## Example

```python
from odin_sdk.models.ai_job_types_response import AIJobTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIJobTypesResponse from a JSON string
ai_job_types_response_instance = AIJobTypesResponse.from_json(json)
# print the JSON string representation of the object
print(AIJobTypesResponse.to_json())

# convert the object into a dict
ai_job_types_response_dict = ai_job_types_response_instance.to_dict()
# create an instance of AIJobTypesResponse from a dict
ai_job_types_response_from_dict = AIJobTypesResponse.from_dict(ai_job_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


