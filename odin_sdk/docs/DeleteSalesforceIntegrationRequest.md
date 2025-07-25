# DeleteSalesforceIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_salesforce_integration_request import DeleteSalesforceIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSalesforceIntegrationRequest from a JSON string
delete_salesforce_integration_request_instance = DeleteSalesforceIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSalesforceIntegrationRequest.to_json())

# convert the object into a dict
delete_salesforce_integration_request_dict = delete_salesforce_integration_request_instance.to_dict()
# create an instance of DeleteSalesforceIntegrationRequest from a dict
delete_salesforce_integration_request_from_dict = DeleteSalesforceIntegrationRequest.from_dict(delete_salesforce_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


