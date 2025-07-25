# InsertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.insert_response import InsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsertResponse from a JSON string
insert_response_instance = InsertResponse.from_json(json)
# print the JSON string representation of the object
print(InsertResponse.to_json())

# convert the object into a dict
insert_response_dict = insert_response_instance.to_dict()
# create an instance of InsertResponse from a dict
insert_response_from_dict = InsertResponse.from_dict(insert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


