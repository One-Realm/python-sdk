# ValidationResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**first_run** | [**ValidationResult**](ValidationResult.md) |  | 
**second_run** | [**ValidationResult**](ValidationResult.md) |  | 
**data_type_schema** | **object** |  | 
**consistent_between_runs** | **bool** |  | 

## Example

```python
from odin_sdk.models.validation_result_response import ValidationResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResultResponse from a JSON string
validation_result_response_instance = ValidationResultResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationResultResponse.to_json())

# convert the object into a dict
validation_result_response_dict = validation_result_response_instance.to_dict()
# create an instance of ValidationResultResponse from a dict
validation_result_response_from_dict = ValidationResultResponse.from_dict(validation_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


