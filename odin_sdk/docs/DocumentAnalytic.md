# DocumentAnalytic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**count** | **int** |  | 
**size** | **int** |  | 
**word_count** | **int** |  | 
**resource_type** | **str** |  | 

## Example

```python
from odin_sdk.models.document_analytic import DocumentAnalytic

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAnalytic from a JSON string
document_analytic_instance = DocumentAnalytic.from_json(json)
# print the JSON string representation of the object
print(DocumentAnalytic.to_json())

# convert the object into a dict
document_analytic_dict = document_analytic_instance.to_dict()
# create an instance of DocumentAnalytic from a dict
document_analytic_from_dict = DocumentAnalytic.from_dict(document_analytic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


