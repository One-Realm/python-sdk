# DeletePersonalityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_personality_request import DeletePersonalityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePersonalityRequest from a JSON string
delete_personality_request_instance = DeletePersonalityRequest.from_json(json)
# print the JSON string representation of the object
print(DeletePersonalityRequest.to_json())

# convert the object into a dict
delete_personality_request_dict = delete_personality_request_instance.to_dict()
# create an instance of DeletePersonalityRequest from a dict
delete_personality_request_from_dict = DeletePersonalityRequest.from_dict(delete_personality_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


