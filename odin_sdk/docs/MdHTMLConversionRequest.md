# MdHTMLConversionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | &#39;markdown&#39; for HTML to Markdown conversion, &#39;html&#39; for Markdown to HTML conversion. | 
**content** | **str** | The content to be converted. | 
**fix_markdown_tabs** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.md_html_conversion_request import MdHTMLConversionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MdHTMLConversionRequest from a JSON string
md_html_conversion_request_instance = MdHTMLConversionRequest.from_json(json)
# print the JSON string representation of the object
print(MdHTMLConversionRequest.to_json())

# convert the object into a dict
md_html_conversion_request_dict = md_html_conversion_request_instance.to_dict()
# create an instance of MdHTMLConversionRequest from a dict
md_html_conversion_request_from_dict = MdHTMLConversionRequest.from_dict(md_html_conversion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


