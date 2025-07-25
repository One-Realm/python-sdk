# ReadNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_all** | **bool** |  | 
**notification_ids** | **List[str]** |  | [optional] 

## Example

```python
from odin_sdk.models.read_notifications_request import ReadNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReadNotificationsRequest from a JSON string
read_notifications_request_instance = ReadNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(ReadNotificationsRequest.to_json())

# convert the object into a dict
read_notifications_request_dict = read_notifications_request_instance.to_dict()
# create an instance of ReadNotificationsRequest from a dict
read_notifications_request_from_dict = ReadNotificationsRequest.from_dict(read_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


