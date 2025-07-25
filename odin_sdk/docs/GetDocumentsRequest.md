# GetDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_documents_request import GetDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentsRequest from a JSON string
get_documents_request_instance = GetDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDocumentsRequest.to_json())

# convert the object into a dict
get_documents_request_dict = get_documents_request_instance.to_dict()
# create an instance of GetDocumentsRequest from a dict
get_documents_request_from_dict = GetDocumentsRequest.from_dict(get_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


