# DocumentChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The chunk content | 
**id** | **int** | The chunk id | 

## Example

```python
from odin_sdk.models.document_chunk import DocumentChunk

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentChunk from a JSON string
document_chunk_instance = DocumentChunk.from_json(json)
# print the JSON string representation of the object
print(DocumentChunk.to_json())

# convert the object into a dict
document_chunk_dict = document_chunk_instance.to_dict()
# create an instance of DocumentChunk from a dict
document_chunk_from_dict = DocumentChunk.from_dict(document_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


