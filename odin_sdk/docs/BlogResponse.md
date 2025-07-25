# BlogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**blog** | [**Blog**](Blog.md) |  | 

## Example

```python
from odin_sdk.models.blog_response import BlogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlogResponse from a JSON string
blog_response_instance = BlogResponse.from_json(json)
# print the JSON string representation of the object
print(BlogResponse.to_json())

# convert the object into a dict
blog_response_dict = blog_response_instance.to_dict()
# create an instance of BlogResponse from a dict
blog_response_from_dict = BlogResponse.from_dict(blog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


