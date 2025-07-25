# TeamTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.team_tag_response import TeamTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamTagResponse from a JSON string
team_tag_response_instance = TeamTagResponse.from_json(json)
# print the JSON string representation of the object
print(TeamTagResponse.to_json())

# convert the object into a dict
team_tag_response_dict = team_tag_response_instance.to_dict()
# create an instance of TeamTagResponse from a dict
team_tag_response_from_dict = TeamTagResponse.from_dict(team_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


