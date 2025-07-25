# AddColumnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**column_name** | **str** |  | 

## Example

```python
from odin_sdk.models.add_column_response import AddColumnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddColumnResponse from a JSON string
add_column_response_instance = AddColumnResponse.from_json(json)
# print the JSON string representation of the object
print(AddColumnResponse.to_json())

# convert the object into a dict
add_column_response_dict = add_column_response_instance.to_dict()
# create an instance of AddColumnResponse from a dict
add_column_response_from_dict = AddColumnResponse.from_dict(add_column_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


