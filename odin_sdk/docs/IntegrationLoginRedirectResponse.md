# IntegrationLoginRedirectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | URL to authorize the OAuth token. | 

## Example

```python
from odin_sdk.models.integration_login_redirect_response import IntegrationLoginRedirectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationLoginRedirectResponse from a JSON string
integration_login_redirect_response_instance = IntegrationLoginRedirectResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationLoginRedirectResponse.to_json())

# convert the object into a dict
integration_login_redirect_response_dict = integration_login_redirect_response_instance.to_dict()
# create an instance of IntegrationLoginRedirectResponse from a dict
integration_login_redirect_response_from_dict = IntegrationLoginRedirectResponse.from_dict(integration_login_redirect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


