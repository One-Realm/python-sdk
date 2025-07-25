# BlogRegenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**blog** | [**Blog**](Blog.md) |  | 
**to_regenerate** | **str** | The string to regenerate | 
**regen_type** | **str** | Type of content to regenerate. Can be &#39;title&#39;, &#39;section&#39;, or &#39;key point&#39; | 

## Example

```python
from odin_sdk.models.blog_regenerate_request import BlogRegenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlogRegenerateRequest from a JSON string
blog_regenerate_request_instance = BlogRegenerateRequest.from_json(json)
# print the JSON string representation of the object
print(BlogRegenerateRequest.to_json())

# convert the object into a dict
blog_regenerate_request_dict = blog_regenerate_request_instance.to_dict()
# create an instance of BlogRegenerateRequest from a dict
blog_regenerate_request_from_dict = BlogRegenerateRequest.from_dict(blog_regenerate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


