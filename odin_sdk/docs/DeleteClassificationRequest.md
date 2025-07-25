# DeleteClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**classification_id** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_classification_request import DeleteClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteClassificationRequest from a JSON string
delete_classification_request_instance = DeleteClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteClassificationRequest.to_json())

# convert the object into a dict
delete_classification_request_dict = delete_classification_request_instance.to_dict()
# create an instance of DeleteClassificationRequest from a dict
delete_classification_request_from_dict = DeleteClassificationRequest.from_dict(delete_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


