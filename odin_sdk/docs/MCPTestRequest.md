# MCPTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | Name of the MCP server to test | 
**transport** | **str** | Transport type (stdio, streamable_http, or sse) | 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from odin_sdk.models.mcp_test_request import MCPTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPTestRequest from a JSON string
mcp_test_request_instance = MCPTestRequest.from_json(json)
# print the JSON string representation of the object
print(MCPTestRequest.to_json())

# convert the object into a dict
mcp_test_request_dict = mcp_test_request_instance.to_dict()
# create an instance of MCPTestRequest from a dict
mcp_test_request_from_dict = MCPTestRequest.from_dict(mcp_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


