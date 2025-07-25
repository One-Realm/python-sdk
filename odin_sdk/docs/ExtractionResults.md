# ExtractionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_results** | [**List[PageExtractionResults]**](PageExtractionResults.md) |  | 
**final_result** | [**FinalResult**](FinalResult.md) |  | 
**overall_accuracy** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.extraction_results import ExtractionResults

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionResults from a JSON string
extraction_results_instance = ExtractionResults.from_json(json)
# print the JSON string representation of the object
print(ExtractionResults.to_json())

# convert the object into a dict
extraction_results_dict = extraction_results_instance.to_dict()
# create an instance of ExtractionResults from a dict
extraction_results_from_dict = ExtractionResults.from_dict(extraction_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


