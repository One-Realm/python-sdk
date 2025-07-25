# ApiToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the API request was successful | 
**message** | **str** | A message describing the result | 
**response** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.api_tool_response import ApiToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToolResponse from a JSON string
api_tool_response_instance = ApiToolResponse.from_json(json)
# print the JSON string representation of the object
print(ApiToolResponse.to_json())

# convert the object into a dict
api_tool_response_dict = api_tool_response_instance.to_dict()
# create an instance of ApiToolResponse from a dict
api_tool_response_from_dict = ApiToolResponse.from_dict(api_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


