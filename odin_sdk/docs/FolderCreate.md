# FolderCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from odin_sdk.models.folder_create import FolderCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FolderCreate from a JSON string
folder_create_instance = FolderCreate.from_json(json)
# print the JSON string representation of the object
print(FolderCreate.to_json())

# convert the object into a dict
folder_create_dict = folder_create_instance.to_dict()
# create an instance of FolderCreate from a dict
folder_create_from_dict = FolderCreate.from_dict(folder_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


