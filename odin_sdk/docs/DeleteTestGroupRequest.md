# DeleteTestGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**test_group_id** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_test_group_request import DeleteTestGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTestGroupRequest from a JSON string
delete_test_group_request_instance = DeleteTestGroupRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTestGroupRequest.to_json())

# convert the object into a dict
delete_test_group_request_dict = delete_test_group_request_instance.to_dict()
# create an instance of DeleteTestGroupRequest from a dict
delete_test_group_request_from_dict = DeleteTestGroupRequest.from_dict(delete_test_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


