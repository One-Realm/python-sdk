# CreateViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the view | 
**description** | **str** |  | [optional] 
**type** | **str** | Type of view (grid, kanban, etc) | [optional] [default to 'grid']
**sort** | **object** |  | [optional] 
**filter** | **object** |  | [optional] 
**group** | **object** |  | [optional] 
**options** | **object** |  | [optional] 
**settings** | **object** |  | [optional] 
**column_meta** | **object** |  | [optional] 
**enable_share** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.create_view_request import CreateViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateViewRequest from a JSON string
create_view_request_instance = CreateViewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateViewRequest.to_json())

# convert the object into a dict
create_view_request_dict = create_view_request_instance.to_dict()
# create an instance of CreateViewRequest from a dict
create_view_request_from_dict = CreateViewRequest.from_dict(create_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


