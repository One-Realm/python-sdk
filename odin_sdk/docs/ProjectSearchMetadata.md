# ProjectSearchMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type** | **str** |  | [optional] 
**upload_date** | **float** |  | [optional] 
**entity_names** | **List[str]** |  | [optional] 
**entity_types** | **List[str]** |  | [optional] 
**entity_salience** | **float** |  | [optional] 
**entity_readability** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.project_search_metadata import ProjectSearchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchMetadata from a JSON string
project_search_metadata_instance = ProjectSearchMetadata.from_json(json)
# print the JSON string representation of the object
print(ProjectSearchMetadata.to_json())

# convert the object into a dict
project_search_metadata_dict = project_search_metadata_instance.to_dict()
# create an instance of ProjectSearchMetadata from a dict
project_search_metadata_from_dict = ProjectSearchMetadata.from_dict(project_search_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


