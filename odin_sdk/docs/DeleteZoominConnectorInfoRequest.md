# DeleteZoominConnectorInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to delete the Zoomin connector info. | 
**uid** | **str** | ID for which to delete the Zoomin connector info. | 
**zoomin_root_web_url** | **str** | Zoomin root web URL. | 

## Example

```python
from odin_sdk.models.delete_zoomin_connector_info_request import DeleteZoominConnectorInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteZoominConnectorInfoRequest from a JSON string
delete_zoomin_connector_info_request_instance = DeleteZoominConnectorInfoRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteZoominConnectorInfoRequest.to_json())

# convert the object into a dict
delete_zoomin_connector_info_request_dict = delete_zoomin_connector_info_request_instance.to_dict()
# create an instance of DeleteZoominConnectorInfoRequest from a dict
delete_zoomin_connector_info_request_from_dict = DeleteZoominConnectorInfoRequest.from_dict(delete_zoomin_connector_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


