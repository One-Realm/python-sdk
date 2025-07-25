# SharePointOauthData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** | Type of the SharePoint OAuth token. | 
**expires_in** | **int** | Expiration time of the SharePoint OAuth token. | 
**ext_expires_in** | **int** |  | 
**access_token** | **str** | Access token for the SharePoint OAuth token. | 

## Example

```python
from odin_sdk.models.share_point_oauth_data import SharePointOauthData

# TODO update the JSON string below
json = "{}"
# create an instance of SharePointOauthData from a JSON string
share_point_oauth_data_instance = SharePointOauthData.from_json(json)
# print the JSON string representation of the object
print(SharePointOauthData.to_json())

# convert the object into a dict
share_point_oauth_data_dict = share_point_oauth_data_instance.to_dict()
# create an instance of SharePointOauthData from a dict
share_point_oauth_data_from_dict = SharePointOauthData.from_dict(share_point_oauth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


