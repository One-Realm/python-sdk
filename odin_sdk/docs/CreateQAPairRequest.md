# CreateQAPairRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**answer** | **str** |  | 
**context** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**doc_key** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_qa_pair_request import CreateQAPairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQAPairRequest from a JSON string
create_qa_pair_request_instance = CreateQAPairRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQAPairRequest.to_json())

# convert the object into a dict
create_qa_pair_request_dict = create_qa_pair_request_instance.to_dict()
# create an instance of CreateQAPairRequest from a dict
create_qa_pair_request_from_dict = CreateQAPairRequest.from_dict(create_qa_pair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


