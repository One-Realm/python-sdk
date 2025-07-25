# BulkUpdateQnARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.bulk_update_qn_a_request import BulkUpdateQnARequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateQnARequest from a JSON string
bulk_update_qn_a_request_instance = BulkUpdateQnARequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateQnARequest.to_json())

# convert the object into a dict
bulk_update_qn_a_request_dict = bulk_update_qn_a_request_instance.to_dict()
# create an instance of BulkUpdateQnARequest from a dict
bulk_update_qn_a_request_from_dict = BulkUpdateQnARequest.from_dict(bulk_update_qn_a_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


