# CreateBlogSectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog_section** | **str** |  | 
**topic_model** | [**TopicModel**](TopicModel.md) |  | 

## Example

```python
from odin_sdk.models.create_blog_section_response import CreateBlogSectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlogSectionResponse from a JSON string
create_blog_section_response_instance = CreateBlogSectionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBlogSectionResponse.to_json())

# convert the object into a dict
create_blog_section_response_dict = create_blog_section_response_instance.to_dict()
# create an instance of CreateBlogSectionResponse from a dict
create_blog_section_response_from_dict = CreateBlogSectionResponse.from_dict(create_blog_section_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


