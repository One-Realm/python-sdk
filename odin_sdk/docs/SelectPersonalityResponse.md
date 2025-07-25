# SelectPersonalityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**system_prompt** | [**SystemPromptData**](SystemPromptData.md) |  | 

## Example

```python
from odin_sdk.models.select_personality_response import SelectPersonalityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelectPersonalityResponse from a JSON string
select_personality_response_instance = SelectPersonalityResponse.from_json(json)
# print the JSON string representation of the object
print(SelectPersonalityResponse.to_json())

# convert the object into a dict
select_personality_response_dict = select_personality_response_instance.to_dict()
# create an instance of SelectPersonalityResponse from a dict
select_personality_response_from_dict = SelectPersonalityResponse.from_dict(select_personality_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


