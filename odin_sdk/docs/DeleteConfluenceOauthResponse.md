# DeleteConfluenceOauthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.delete_confluence_oauth_response import DeleteConfluenceOauthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteConfluenceOauthResponse from a JSON string
delete_confluence_oauth_response_instance = DeleteConfluenceOauthResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteConfluenceOauthResponse.to_json())

# convert the object into a dict
delete_confluence_oauth_response_dict = delete_confluence_oauth_response_instance.to_dict()
# create an instance of DeleteConfluenceOauthResponse from a dict
delete_confluence_oauth_response_from_dict = DeleteConfluenceOauthResponse.from_dict(delete_confluence_oauth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


