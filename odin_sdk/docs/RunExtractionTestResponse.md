# RunExtractionTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**results** | [**ExtractionResults**](ExtractionResults.md) |  | 
**result_type** | **str** |  | [optional] 
**should_provide_validation_score** | **bool** |  | [optional] [default to False]

## Example

```python
from odin_sdk.models.run_extraction_test_response import RunExtractionTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunExtractionTestResponse from a JSON string
run_extraction_test_response_instance = RunExtractionTestResponse.from_json(json)
# print the JSON string representation of the object
print(RunExtractionTestResponse.to_json())

# convert the object into a dict
run_extraction_test_response_dict = run_extraction_test_response_instance.to_dict()
# create an instance of RunExtractionTestResponse from a dict
run_extraction_test_response_from_dict = RunExtractionTestResponse.from_dict(run_extraction_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


