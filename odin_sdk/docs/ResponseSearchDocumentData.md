# ResponseSearchDocumentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_key** | **str** | The content key of the document - either full URL in case of web links stored in the KB or full filename, e.g. &#39;example.pdf&#39;. | 
**metadata** | **object** | The metadata of the document. | 

## Example

```python
from odin_sdk.models.response_search_document_data import ResponseSearchDocumentData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSearchDocumentData from a JSON string
response_search_document_data_instance = ResponseSearchDocumentData.from_json(json)
# print the JSON string representation of the object
print(ResponseSearchDocumentData.to_json())

# convert the object into a dict
response_search_document_data_dict = response_search_document_data_instance.to_dict()
# create an instance of ResponseSearchDocumentData from a dict
response_search_document_data_from_dict = ResponseSearchDocumentData.from_dict(response_search_document_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


