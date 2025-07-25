# DeleteConfluenceOauthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to delete the Confluence OAuth credentials. | 
**uid** | **str** | User ID for which to delete the Confluence OAuth credentials. | 

## Example

```python
from odin_sdk.models.delete_confluence_oauth_request import DeleteConfluenceOauthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConfluenceOauthRequest from a JSON string
delete_confluence_oauth_request_instance = DeleteConfluenceOauthRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteConfluenceOauthRequest.to_json())

# convert the object into a dict
delete_confluence_oauth_request_dict = delete_confluence_oauth_request_instance.to_dict()
# create an instance of DeleteConfluenceOauthRequest from a dict
delete_confluence_oauth_request_from_dict = DeleteConfluenceOauthRequest.from_dict(delete_confluence_oauth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


