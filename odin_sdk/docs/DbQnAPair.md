# DbQnAPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**answer** | **str** |  | 
**type** | **str** |  | [optional] 
**id** | **str** |  | 
**status** | **str** |  | [optional] 
**created_at** | **float** |  | [optional] 
**context** | **str** |  | [optional] 
**associated_file** | **str** |  | [optional] 
**auto_generated** | **bool** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**project_id** | **str** |  | [optional] 
**embedding_record_id** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.db_qn_a_pair import DbQnAPair

# TODO update the JSON string below
json = "{}"
# create an instance of DbQnAPair from a JSON string
db_qn_a_pair_instance = DbQnAPair.from_json(json)
# print the JSON string representation of the object
print(DbQnAPair.to_json())

# convert the object into a dict
db_qn_a_pair_dict = db_qn_a_pair_instance.to_dict()
# create an instance of DbQnAPair from a dict
db_qn_a_pair_from_dict = DbQnAPair.from_dict(db_qn_a_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


