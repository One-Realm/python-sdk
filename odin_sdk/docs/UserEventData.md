# UserEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**credits_used** | **int** |  | 
**timestamp** | **float** |  | 
**event_type** | **str** |  | 

## Example

```python
from odin_sdk.models.user_event_data import UserEventData

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventData from a JSON string
user_event_data_instance = UserEventData.from_json(json)
# print the JSON string representation of the object
print(UserEventData.to_json())

# convert the object into a dict
user_event_data_dict = user_event_data_instance.to_dict()
# create an instance of UserEventData from a dict
user_event_data_from_dict = UserEventData.from_dict(user_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


