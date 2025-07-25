# SaveOnPremConfluenceConnectorInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to save the OnPrem Confluence connector info. | 
**root_url** | **str** | OnPrem Confluence root URL. | 
**bearer_token** | **str** | OnPrem Confluence bearer token. | 

## Example

```python
from odin_sdk.models.save_on_prem_confluence_connector_info_request import SaveOnPremConfluenceConnectorInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveOnPremConfluenceConnectorInfoRequest from a JSON string
save_on_prem_confluence_connector_info_request_instance = SaveOnPremConfluenceConnectorInfoRequest.from_json(json)
# print the JSON string representation of the object
print(SaveOnPremConfluenceConnectorInfoRequest.to_json())

# convert the object into a dict
save_on_prem_confluence_connector_info_request_dict = save_on_prem_confluence_connector_info_request_instance.to_dict()
# create an instance of SaveOnPremConfluenceConnectorInfoRequest from a dict
save_on_prem_confluence_connector_info_request_from_dict = SaveOnPremConfluenceConnectorInfoRequest.from_dict(save_on_prem_confluence_connector_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


