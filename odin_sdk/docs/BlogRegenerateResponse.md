# BlogRegenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**regenerated_options** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.blog_regenerate_response import BlogRegenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlogRegenerateResponse from a JSON string
blog_regenerate_response_instance = BlogRegenerateResponse.from_json(json)
# print the JSON string representation of the object
print(BlogRegenerateResponse.to_json())

# convert the object into a dict
blog_regenerate_response_dict = blog_regenerate_response_instance.to_dict()
# create an instance of BlogRegenerateResponse from a dict
blog_regenerate_response_from_dict = BlogRegenerateResponse.from_dict(blog_regenerate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


