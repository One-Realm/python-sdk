# BlogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**blog** | [**Blog**](Blog.md) |  | 

## Example

```python
from odin_sdk.models.blog_request import BlogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlogRequest from a JSON string
blog_request_instance = BlogRequest.from_json(json)
# print the JSON string representation of the object
print(BlogRequest.to_json())

# convert the object into a dict
blog_request_dict = blog_request_instance.to_dict()
# create an instance of BlogRequest from a dict
blog_request_from_dict = BlogRequest.from_dict(blog_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


