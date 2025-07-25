# AddPersonalityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**instructions** | **str** |  | 
**type** | **str** |  | 
**project_id** | **str** |  | 
**temperature** | **float** |  | 

## Example

```python
from odin_sdk.models.add_personality_request import AddPersonalityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonalityRequest from a JSON string
add_personality_request_instance = AddPersonalityRequest.from_json(json)
# print the JSON string representation of the object
print(AddPersonalityRequest.to_json())

# convert the object into a dict
add_personality_request_dict = add_personality_request_instance.to_dict()
# create an instance of AddPersonalityRequest from a dict
add_personality_request_from_dict = AddPersonalityRequest.from_dict(add_personality_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


