# DeleteTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_team_request import DeleteTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTeamRequest from a JSON string
delete_team_request_instance = DeleteTeamRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTeamRequest.to_json())

# convert the object into a dict
delete_team_request_dict = delete_team_request_instance.to_dict()
# create an instance of DeleteTeamRequest from a dict
delete_team_request_from_dict = DeleteTeamRequest.from_dict(delete_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


