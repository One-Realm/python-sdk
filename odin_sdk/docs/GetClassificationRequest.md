# GetClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**classification_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_classification_request import GetClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetClassificationRequest from a JSON string
get_classification_request_instance = GetClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(GetClassificationRequest.to_json())

# convert the object into a dict
get_classification_request_dict = get_classification_request_instance.to_dict()
# create an instance of GetClassificationRequest from a dict
get_classification_request_from_dict = GetClassificationRequest.from_dict(get_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


