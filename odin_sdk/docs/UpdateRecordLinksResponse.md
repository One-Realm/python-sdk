# UpdateRecordLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**updated** | **bool** |  | 

## Example

```python
from odin_sdk.models.update_record_links_response import UpdateRecordLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordLinksResponse from a JSON string
update_record_links_response_instance = UpdateRecordLinksResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordLinksResponse.to_json())

# convert the object into a dict
update_record_links_response_dict = update_record_links_response_instance.to_dict()
# create an instance of UpdateRecordLinksResponse from a dict
update_record_links_response_from_dict = UpdateRecordLinksResponse.from_dict(update_record_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


