# RegisterNewBotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**app_password** | **str** |  | 

## Example

```python
from odin_sdk.models.register_new_bot_request import RegisterNewBotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterNewBotRequest from a JSON string
register_new_bot_request_instance = RegisterNewBotRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterNewBotRequest.to_json())

# convert the object into a dict
register_new_bot_request_dict = register_new_bot_request_instance.to_dict()
# create an instance of RegisterNewBotRequest from a dict
register_new_bot_request_from_dict = RegisterNewBotRequest.from_dict(register_new_bot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


