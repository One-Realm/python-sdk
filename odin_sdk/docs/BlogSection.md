# BlogSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**content** | **str** |  | [optional] [default to '']
**ideas** | **List[str]** |  | [optional] [default to []]

## Example

```python
from odin_sdk.models.blog_section import BlogSection

# TODO update the JSON string below
json = "{}"
# create an instance of BlogSection from a JSON string
blog_section_instance = BlogSection.from_json(json)
# print the JSON string representation of the object
print(BlogSection.to_json())

# convert the object into a dict
blog_section_dict = blog_section_instance.to_dict()
# create an instance of BlogSection from a dict
blog_section_from_dict = BlogSection.from_dict(blog_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


