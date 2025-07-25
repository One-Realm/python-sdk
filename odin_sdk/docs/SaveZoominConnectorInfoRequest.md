# SaveZoominConnectorInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to save the Zoomin connector info. | 
**zoomin_root_api_url** | **str** | Zoomin root API URL. | 
**zoomin_root_web_url** | **str** | Zoomin root web URL. | 
**zoomin_bearer_token** | **str** | Zoomin bearer token. | 

## Example

```python
from odin_sdk.models.save_zoomin_connector_info_request import SaveZoominConnectorInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveZoominConnectorInfoRequest from a JSON string
save_zoomin_connector_info_request_instance = SaveZoominConnectorInfoRequest.from_json(json)
# print the JSON string representation of the object
print(SaveZoominConnectorInfoRequest.to_json())

# convert the object into a dict
save_zoomin_connector_info_request_dict = save_zoomin_connector_info_request_instance.to_dict()
# create an instance of SaveZoominConnectorInfoRequest from a dict
save_zoomin_connector_info_request_from_dict = SaveZoominConnectorInfoRequest.from_dict(save_zoomin_connector_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


