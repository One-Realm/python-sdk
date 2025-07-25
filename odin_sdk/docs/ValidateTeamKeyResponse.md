# ValidateTeamKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **bool** |  | 
**msg** | **str** |  | 

## Example

```python
from odin_sdk.models.validate_team_key_response import ValidateTeamKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTeamKeyResponse from a JSON string
validate_team_key_response_instance = ValidateTeamKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateTeamKeyResponse.to_json())

# convert the object into a dict
validate_team_key_response_dict = validate_team_key_response_instance.to_dict()
# create an instance of ValidateTeamKeyResponse from a dict
validate_team_key_response_from_dict = ValidateTeamKeyResponse.from_dict(validate_team_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


