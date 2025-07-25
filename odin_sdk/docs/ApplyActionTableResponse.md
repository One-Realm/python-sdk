# ApplyActionTableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message | 
**processed_rows** | **int** | Number of rows processed | 

## Example

```python
from odin_sdk.models.apply_action_table_response import ApplyActionTableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyActionTableResponse from a JSON string
apply_action_table_response_instance = ApplyActionTableResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyActionTableResponse.to_json())

# convert the object into a dict
apply_action_table_response_dict = apply_action_table_response_instance.to_dict()
# create an instance of ApplyActionTableResponse from a dict
apply_action_table_response_from_dict = ApplyActionTableResponse.from_dict(apply_action_table_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


