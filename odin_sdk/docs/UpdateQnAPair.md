# UpdateQnAPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**answer** | **str** |  | [optional] 
**context** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**associated_file** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.update_qn_a_pair import UpdateQnAPair

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQnAPair from a JSON string
update_qn_a_pair_instance = UpdateQnAPair.from_json(json)
# print the JSON string representation of the object
print(UpdateQnAPair.to_json())

# convert the object into a dict
update_qn_a_pair_dict = update_qn_a_pair_instance.to_dict()
# create an instance of UpdateQnAPair from a dict
update_qn_a_pair_from_dict = UpdateQnAPair.from_dict(update_qn_a_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


