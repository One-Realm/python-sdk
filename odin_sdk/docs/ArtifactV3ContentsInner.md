# ArtifactV3ContentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**type** | **str** |  | 
**title** | **str** |  | 
**full_markdown** | **str** |  | 
**language** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from odin_sdk.models.artifact_v3_contents_inner import ArtifactV3ContentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactV3ContentsInner from a JSON string
artifact_v3_contents_inner_instance = ArtifactV3ContentsInner.from_json(json)
# print the JSON string representation of the object
print(ArtifactV3ContentsInner.to_json())

# convert the object into a dict
artifact_v3_contents_inner_dict = artifact_v3_contents_inner_instance.to_dict()
# create an instance of ArtifactV3ContentsInner from a dict
artifact_v3_contents_inner_from_dict = ArtifactV3ContentsInner.from_dict(artifact_v3_contents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


