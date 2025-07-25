# Blog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**keywords** | **List[str]** |  | [optional] [default to []]
**goal** | **str** |  | [optional] [default to '']
**final_content** | **str** |  | [optional] [default to '']
**sections** | [**List[BlogSection]**](BlogSection.md) |  | [optional] [default to []]

## Example

```python
from odin_sdk.models.blog import Blog

# TODO update the JSON string below
json = "{}"
# create an instance of Blog from a JSON string
blog_instance = Blog.from_json(json)
# print the JSON string representation of the object
print(Blog.to_json())

# convert the object into a dict
blog_dict = blog_instance.to_dict()
# create an instance of Blog from a dict
blog_from_dict = Blog.from_dict(blog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


