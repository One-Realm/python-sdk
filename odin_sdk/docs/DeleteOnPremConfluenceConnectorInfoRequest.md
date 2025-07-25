# DeleteOnPremConfluenceConnectorInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to delete the OnPrem Confluence connector info. | 
**root_url** | **str** | OnPrem Confluence root URL. | 

## Example

```python
from odin_sdk.models.delete_on_prem_confluence_connector_info_request import DeleteOnPremConfluenceConnectorInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOnPremConfluenceConnectorInfoRequest from a JSON string
delete_on_prem_confluence_connector_info_request_instance = DeleteOnPremConfluenceConnectorInfoRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOnPremConfluenceConnectorInfoRequest.to_json())

# convert the object into a dict
delete_on_prem_confluence_connector_info_request_dict = delete_on_prem_confluence_connector_info_request_instance.to_dict()
# create an instance of DeleteOnPremConfluenceConnectorInfoRequest from a dict
delete_on_prem_confluence_connector_info_request_from_dict = DeleteOnPremConfluenceConnectorInfoRequest.from_dict(delete_on_prem_confluence_connector_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


