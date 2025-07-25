# TokenUsage

Model for token usage metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**input_tokens** | **int** |  | 
**output_tokens** | **int** |  | 

## Example

```python
from odin_sdk.models.token_usage import TokenUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TokenUsage from a JSON string
token_usage_instance = TokenUsage.from_json(json)
# print the JSON string representation of the object
print(TokenUsage.to_json())

# convert the object into a dict
token_usage_dict = token_usage_instance.to_dict()
# create an instance of TokenUsage from a dict
token_usage_from_dict = TokenUsage.from_dict(token_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


