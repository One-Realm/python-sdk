# TeamTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.team_tag_request import TeamTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamTagRequest from a JSON string
team_tag_request_instance = TeamTagRequest.from_json(json)
# print the JSON string representation of the object
print(TeamTagRequest.to_json())

# convert the object into a dict
team_tag_request_dict = team_tag_request_instance.to_dict()
# create an instance of TeamTagRequest from a dict
team_tag_request_from_dict = TeamTagRequest.from_dict(team_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


