# BlogRegenerateSectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**blog** | [**Blog**](Blog.md) |  | 
**blog_section_index** | **int** |  | 

## Example

```python
from odin_sdk.models.blog_regenerate_section_request import BlogRegenerateSectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlogRegenerateSectionRequest from a JSON string
blog_regenerate_section_request_instance = BlogRegenerateSectionRequest.from_json(json)
# print the JSON string representation of the object
print(BlogRegenerateSectionRequest.to_json())

# convert the object into a dict
blog_regenerate_section_request_dict = blog_regenerate_section_request_instance.to_dict()
# create an instance of BlogRegenerateSectionRequest from a dict
blog_regenerate_section_request_from_dict = BlogRegenerateSectionRequest.from_dict(blog_regenerate_section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


