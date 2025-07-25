# UpdateRecordLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | The name of the collection column | 
**target_ids** | **List[int]** | The IDs of the target records to link | 

## Example

```python
from odin_sdk.models.update_record_links_request import UpdateRecordLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordLinksRequest from a JSON string
update_record_links_request_instance = UpdateRecordLinksRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordLinksRequest.to_json())

# convert the object into a dict
update_record_links_request_dict = update_record_links_request_instance.to_dict()
# create an instance of UpdateRecordLinksRequest from a dict
update_record_links_request_from_dict = UpdateRecordLinksRequest.from_dict(update_record_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


