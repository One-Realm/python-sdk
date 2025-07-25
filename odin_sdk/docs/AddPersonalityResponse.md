# AddPersonalityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personality_id** | **str** |  | 
**name** | **str** |  | 
**instructions** | **str** |  | 
**type** | **str** |  | 
**temperature** | **float** |  | 
**updated_at** | **float** |  | 

## Example

```python
from odin_sdk.models.add_personality_response import AddPersonalityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonalityResponse from a JSON string
add_personality_response_instance = AddPersonalityResponse.from_json(json)
# print the JSON string representation of the object
print(AddPersonalityResponse.to_json())

# convert the object into a dict
add_personality_response_dict = add_personality_response_instance.to_dict()
# create an instance of AddPersonalityResponse from a dict
add_personality_response_from_dict = AddPersonalityResponse.from_dict(add_personality_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


