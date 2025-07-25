# SelectPersonalityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**name** | **str** |  | 
**instructions** | **str** |  | 
**temperature** | **float** |  | 
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from odin_sdk.models.select_personality_request import SelectPersonalityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelectPersonalityRequest from a JSON string
select_personality_request_instance = SelectPersonalityRequest.from_json(json)
# print the JSON string representation of the object
print(SelectPersonalityRequest.to_json())

# convert the object into a dict
select_personality_request_dict = select_personality_request_instance.to_dict()
# create an instance of SelectPersonalityRequest from a dict
select_personality_request_from_dict = SelectPersonalityRequest.from_dict(select_personality_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


