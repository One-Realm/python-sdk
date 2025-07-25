# UpdateRowOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_index** | **int** | The current row_index of the row to move | 
**new_index** | **int** | The new desired row_index for the row | 

## Example

```python
from odin_sdk.models.update_row_order_request import UpdateRowOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRowOrderRequest from a JSON string
update_row_order_request_instance = UpdateRowOrderRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRowOrderRequest.to_json())

# convert the object into a dict
update_row_order_request_dict = update_row_order_request_instance.to_dict()
# create an instance of UpdateRowOrderRequest from a dict
update_row_order_request_from_dict = UpdateRowOrderRequest.from_dict(update_row_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


