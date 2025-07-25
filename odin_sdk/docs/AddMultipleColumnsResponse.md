# AddMultipleColumnsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**columns_added** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.add_multiple_columns_response import AddMultipleColumnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddMultipleColumnsResponse from a JSON string
add_multiple_columns_response_instance = AddMultipleColumnsResponse.from_json(json)
# print the JSON string representation of the object
print(AddMultipleColumnsResponse.to_json())

# convert the object into a dict
add_multiple_columns_response_dict = add_multiple_columns_response_instance.to_dict()
# create an instance of AddMultipleColumnsResponse from a dict
add_multiple_columns_response_from_dict = AddMultipleColumnsResponse.from_dict(add_multiple_columns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


