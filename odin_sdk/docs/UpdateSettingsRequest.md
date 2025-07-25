# UpdateSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_signups** | **bool** |  | [optional] 
**team_name** | **str** |  | [optional] 
**disable_meetings** | **bool** |  | [optional] 
**default_project_id** | **str** |  | [optional] 
**aihub_projects_whitelist** | **List[str]** |  | [optional] 
**auto_add_users_by_domain** | **bool** |  | [optional] 
**team_email_domain** | **str** |  | [optional] 
**chat_mode_appearance** | **object** |  | [optional] 
**chat_mode_for_members** | **bool** |  | [optional] 
**enable_user_credit_limits** | **bool** |  | [optional] 
**default_user_credit_limit** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from odin_sdk.models.update_settings_request import UpdateSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSettingsRequest from a JSON string
update_settings_request_instance = UpdateSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSettingsRequest.to_json())

# convert the object into a dict
update_settings_request_dict = update_settings_request_instance.to_dict()
# create an instance of UpdateSettingsRequest from a dict
update_settings_request_from_dict = UpdateSettingsRequest.from_dict(update_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


