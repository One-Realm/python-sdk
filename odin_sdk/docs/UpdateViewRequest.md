# UpdateViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sort** | **object** |  | [optional] 
**filter** | **object** |  | [optional] 
**group** | **object** |  | [optional] 
**options** | **object** |  | [optional] 
**settings** | **object** |  | [optional] 
**column_meta** | **object** |  | [optional] 
**enable_share** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_view_request import UpdateViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateViewRequest from a JSON string
update_view_request_instance = UpdateViewRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateViewRequest.to_json())

# convert the object into a dict
update_view_request_dict = update_view_request_instance.to_dict()
# create an instance of UpdateViewRequest from a dict
update_view_request_from_dict = UpdateViewRequest.from_dict(update_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


