# MCPTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**error_details** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.mcp_test_response import MCPTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPTestResponse from a JSON string
mcp_test_response_instance = MCPTestResponse.from_json(json)
# print the JSON string representation of the object
print(MCPTestResponse.to_json())

# convert the object into a dict
mcp_test_response_dict = mcp_test_response_instance.to_dict()
# create an instance of MCPTestResponse from a dict
mcp_test_response_from_dict = MCPTestResponse.from_dict(mcp_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


