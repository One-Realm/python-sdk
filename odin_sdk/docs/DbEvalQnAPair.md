# DbEvalQnAPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**question** | **str** |  | 
**answer** | **str** |  | 
**relevant_chunks** | [**List[RelevantChunks]**](RelevantChunks.md) |  | 
**chunk_ids** | **List[int]** |  | 
**citation_correctness** | **float** |  | [optional] 
**citation_redundancy** | **float** |  | [optional] 
**retrieval_correctness** | **float** |  | [optional] 
**retrieval_precision** | **float** |  | [optional] 
**document_keys** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**project_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.db_eval_qn_a_pair import DbEvalQnAPair

# TODO update the JSON string below
json = "{}"
# create an instance of DbEvalQnAPair from a JSON string
db_eval_qn_a_pair_instance = DbEvalQnAPair.from_json(json)
# print the JSON string representation of the object
print(DbEvalQnAPair.to_json())

# convert the object into a dict
db_eval_qn_a_pair_dict = db_eval_qn_a_pair_instance.to_dict()
# create an instance of DbEvalQnAPair from a dict
db_eval_qn_a_pair_from_dict = DbEvalQnAPair.from_dict(db_eval_qn_a_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


