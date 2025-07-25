# QueryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_text** | **str** |  | 
**doc_ids** | **str** |  | [optional] [default to '[]']

## Example

```python
from odin_sdk.models.query_payload import QueryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPayload from a JSON string
query_payload_instance = QueryPayload.from_json(json)
# print the JSON string representation of the object
print(QueryPayload.to_json())

# convert the object into a dict
query_payload_dict = query_payload_instance.to_dict()
# create an instance of QueryPayload from a dict
query_payload_from_dict = QueryPayload.from_dict(query_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


