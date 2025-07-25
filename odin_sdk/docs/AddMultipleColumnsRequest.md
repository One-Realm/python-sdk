# AddMultipleColumnsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[AddColumnRequest]**](AddColumnRequest.md) | List of columns to add | 

## Example

```python
from odin_sdk.models.add_multiple_columns_request import AddMultipleColumnsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMultipleColumnsRequest from a JSON string
add_multiple_columns_request_instance = AddMultipleColumnsRequest.from_json(json)
# print the JSON string representation of the object
print(AddMultipleColumnsRequest.to_json())

# convert the object into a dict
add_multiple_columns_request_dict = add_multiple_columns_request_instance.to_dict()
# create an instance of AddMultipleColumnsRequest from a dict
add_multiple_columns_request_from_dict = AddMultipleColumnsRequest.from_dict(add_multiple_columns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


