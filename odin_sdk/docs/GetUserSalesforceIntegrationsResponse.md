# GetUserSalesforceIntegrationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[SalesforceIntegration]**](SalesforceIntegration.md) |  | 

## Example

```python
from odin_sdk.models.get_user_salesforce_integrations_response import GetUserSalesforceIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserSalesforceIntegrationsResponse from a JSON string
get_user_salesforce_integrations_response_instance = GetUserSalesforceIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserSalesforceIntegrationsResponse.to_json())

# convert the object into a dict
get_user_salesforce_integrations_response_dict = get_user_salesforce_integrations_response_instance.to_dict()
# create an instance of GetUserSalesforceIntegrationsResponse from a dict
get_user_salesforce_integrations_response_from_dict = GetUserSalesforceIntegrationsResponse.from_dict(get_user_salesforce_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


