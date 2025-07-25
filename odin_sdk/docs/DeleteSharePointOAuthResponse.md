# DeleteSharePointOAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.delete_share_point_o_auth_response import DeleteSharePointOAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSharePointOAuthResponse from a JSON string
delete_share_point_o_auth_response_instance = DeleteSharePointOAuthResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSharePointOAuthResponse.to_json())

# convert the object into a dict
delete_share_point_o_auth_response_dict = delete_share_point_o_auth_response_instance.to_dict()
# create an instance of DeleteSharePointOAuthResponse from a dict
delete_share_point_o_auth_response_from_dict = DeleteSharePointOAuthResponse.from_dict(delete_share_point_o_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


