# RunExtractionTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_document_id** | **str** | ID of the sample document | 
**custom_extraction_config** | **List[object]** | Custom extraction configuration | 

## Example

```python
from odin_sdk.models.run_extraction_test_request import RunExtractionTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunExtractionTestRequest from a JSON string
run_extraction_test_request_instance = RunExtractionTestRequest.from_json(json)
# print the JSON string representation of the object
print(RunExtractionTestRequest.to_json())

# convert the object into a dict
run_extraction_test_request_dict = run_extraction_test_request_instance.to_dict()
# create an instance of RunExtractionTestRequest from a dict
run_extraction_test_request_from_dict = RunExtractionTestRequest.from_dict(run_extraction_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


