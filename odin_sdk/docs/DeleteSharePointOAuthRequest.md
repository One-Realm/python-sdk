# DeleteSharePointOAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to delete the SharePoint OAuth credentials. | 
**uid** | **str** | User ID for which to delete the SharePoint OAuth credentials. | 

## Example

```python
from odin_sdk.models.delete_share_point_o_auth_request import DeleteSharePointOAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSharePointOAuthRequest from a JSON string
delete_share_point_o_auth_request_instance = DeleteSharePointOAuthRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSharePointOAuthRequest.to_json())

# convert the object into a dict
delete_share_point_o_auth_request_dict = delete_share_point_o_auth_request_instance.to_dict()
# create an instance of DeleteSharePointOAuthRequest from a dict
delete_share_point_o_auth_request_from_dict = DeleteSharePointOAuthRequest.from_dict(delete_share_point_o_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


