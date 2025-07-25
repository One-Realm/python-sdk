# UpdateColumnValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**updated_value** | **object** |  | 

## Example

```python
from odin_sdk.models.update_column_value_response import UpdateColumnValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumnValueResponse from a JSON string
update_column_value_response_instance = UpdateColumnValueResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateColumnValueResponse.to_json())

# convert the object into a dict
update_column_value_response_dict = update_column_value_response_instance.to_dict()
# create an instance of UpdateColumnValueResponse from a dict
update_column_value_response_from_dict = UpdateColumnValueResponse.from_dict(update_column_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


