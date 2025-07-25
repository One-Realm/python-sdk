# ProjectVersionSwitchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**version** | **int** |  | 
**force** | **bool** |  | [optional] 
**resume_existing** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.project_version_switch_request import ProjectVersionSwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectVersionSwitchRequest from a JSON string
project_version_switch_request_instance = ProjectVersionSwitchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectVersionSwitchRequest.to_json())

# convert the object into a dict
project_version_switch_request_dict = project_version_switch_request_instance.to_dict()
# create an instance of ProjectVersionSwitchRequest from a dict
project_version_switch_request_from_dict = ProjectVersionSwitchRequest.from_dict(project_version_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


