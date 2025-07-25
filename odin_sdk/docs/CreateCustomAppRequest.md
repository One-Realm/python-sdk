# CreateCustomAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**project_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**thoughts** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.create_custom_app_request import CreateCustomAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomAppRequest from a JSON string
create_custom_app_request_instance = CreateCustomAppRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomAppRequest.to_json())

# convert the object into a dict
create_custom_app_request_dict = create_custom_app_request_instance.to_dict()
# create an instance of CreateCustomAppRequest from a dict
create_custom_app_request_from_dict = CreateCustomAppRequest.from_dict(create_custom_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


