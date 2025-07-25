# Attendee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | 
**is_organizer** | **bool** |  | 
**status** | **str** |  | 

## Example

```python
from odin_sdk.models.attendee import Attendee

# TODO update the JSON string below
json = "{}"
# create an instance of Attendee from a JSON string
attendee_instance = Attendee.from_json(json)
# print the JSON string representation of the object
print(Attendee.to_json())

# convert the object into a dict
attendee_dict = attendee_instance.to_dict()
# create an instance of Attendee from a dict
attendee_from_dict = Attendee.from_dict(attendee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


