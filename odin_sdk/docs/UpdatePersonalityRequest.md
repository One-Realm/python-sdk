# UpdatePersonalityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**instructions** | **str** |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**project_id** | **str** |  | 
**temperature** | **float** |  | 

## Example

```python
from odin_sdk.models.update_personality_request import UpdatePersonalityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePersonalityRequest from a JSON string
update_personality_request_instance = UpdatePersonalityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePersonalityRequest.to_json())

# convert the object into a dict
update_personality_request_dict = update_personality_request_instance.to_dict()
# create an instance of UpdatePersonalityRequest from a dict
update_personality_request_from_dict = UpdatePersonalityRequest.from_dict(update_personality_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


