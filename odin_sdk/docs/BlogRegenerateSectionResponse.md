# BlogRegenerateSectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**blog_section** | [**BlogSection**](BlogSection.md) |  | 

## Example

```python
from odin_sdk.models.blog_regenerate_section_response import BlogRegenerateSectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlogRegenerateSectionResponse from a JSON string
blog_regenerate_section_response_instance = BlogRegenerateSectionResponse.from_json(json)
# print the JSON string representation of the object
print(BlogRegenerateSectionResponse.to_json())

# convert the object into a dict
blog_regenerate_section_response_dict = blog_regenerate_section_response_instance.to_dict()
# create an instance of BlogRegenerateSectionResponse from a dict
blog_regenerate_section_response_from_dict = BlogRegenerateSectionResponse.from_dict(blog_regenerate_section_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


