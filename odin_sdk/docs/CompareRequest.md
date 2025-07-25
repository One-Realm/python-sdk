# CompareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The ID of the project on which to execute the action. | 
**document_1** | **str** |  | [optional] 
**document_2** | **str** |  | [optional] 
**doc_1_content** | **str** |  | [optional] 
**doc_2_content** | **str** |  | [optional] 
**ignore_instructions** | **List[object]** |  | [optional] 
**credit_usage_limit** | **int** |  | [optional] 
**diff_ai_overide_limit** | **int** |  | [optional] 
**sent_from_automator** | **bool** |  | [optional] 
**wait_till_complete** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.compare_request import CompareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompareRequest from a JSON string
compare_request_instance = CompareRequest.from_json(json)
# print the JSON string representation of the object
print(CompareRequest.to_json())

# convert the object into a dict
compare_request_dict = compare_request_instance.to_dict()
# create an instance of CompareRequest from a dict
compare_request_from_dict = CompareRequest.from_dict(compare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


