# ProjectVersionSwitchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_started** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.project_version_switch_response import ProjectVersionSwitchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVersionSwitchResponse from a JSON string
project_version_switch_response_instance = ProjectVersionSwitchResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectVersionSwitchResponse.to_json())

# convert the object into a dict
project_version_switch_response_dict = project_version_switch_response_instance.to_dict()
# create an instance of ProjectVersionSwitchResponse from a dict
project_version_switch_response_from_dict = ProjectVersionSwitchResponse.from_dict(project_version_switch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


