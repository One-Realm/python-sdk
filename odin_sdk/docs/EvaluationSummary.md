# EvaluationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_questions** | **int** |  | 
**avg_retrieval_correctness** | **float** |  | 
**avg_retrieval_precision** | **float** |  | 
**avg_citation_correctness** | **float** |  | 
**avg_citation_redundancy** | **float** |  | 

## Example

```python
from odin_sdk.models.evaluation_summary import EvaluationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationSummary from a JSON string
evaluation_summary_instance = EvaluationSummary.from_json(json)
# print the JSON string representation of the object
print(EvaluationSummary.to_json())

# convert the object into a dict
evaluation_summary_dict = evaluation_summary_instance.to_dict()
# create an instance of EvaluationSummary from a dict
evaluation_summary_from_dict = EvaluationSummary.from_dict(evaluation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


