# CustomToolVersionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[CustomToolVersionResponse]**](CustomToolVersionResponse.md) | List of tool versions | [optional] 
**total** | **int** | Total number of versions | 

## Example

```python
from odin_sdk.models.custom_tool_version_list_response import CustomToolVersionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomToolVersionListResponse from a JSON string
custom_tool_version_list_response_instance = CustomToolVersionListResponse.from_json(json)
# print the JSON string representation of the object
print(CustomToolVersionListResponse.to_json())

# convert the object into a dict
custom_tool_version_list_response_dict = custom_tool_version_list_response_instance.to_dict()
# create an instance of CustomToolVersionListResponse from a dict
custom_tool_version_list_response_from_dict = CustomToolVersionListResponse.from_dict(custom_tool_version_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


