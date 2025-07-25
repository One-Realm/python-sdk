# OpenCanvasGraphAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlighted_code** | [**CodeHighlight**](CodeHighlight.md) |  | [optional] 
**highlighted_text** | [**TextHighlight**](TextHighlight.md) |  | [optional] 
**artifact** | [**ArtifactV3**](ArtifactV3.md) |  | [optional] 
**next** | **str** |  | [optional] 
**language** | [**LanguageOptions**](LanguageOptions.md) |  | [optional] 
**artifact_length** | [**ArtifactLengthOptions**](ArtifactLengthOptions.md) |  | [optional] 
**regenerate_with_emojis** | **bool** |  | [optional] 
**reading_level** | [**ReadingLevelOptions**](ReadingLevelOptions.md) |  | [optional] 
**add_comments** | **bool** |  | [optional] 
**add_logs** | **bool** |  | [optional] 
**port_language** | [**ProgrammingLanguageOptions**](ProgrammingLanguageOptions.md) |  | [optional] 
**fix_bugs** | **bool** |  | [optional] 
**custom_quick_action_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.open_canvas_graph_annotation import OpenCanvasGraphAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of OpenCanvasGraphAnnotation from a JSON string
open_canvas_graph_annotation_instance = OpenCanvasGraphAnnotation.from_json(json)
# print the JSON string representation of the object
print(OpenCanvasGraphAnnotation.to_json())

# convert the object into a dict
open_canvas_graph_annotation_dict = open_canvas_graph_annotation_instance.to_dict()
# create an instance of OpenCanvasGraphAnnotation from a dict
open_canvas_graph_annotation_from_dict = OpenCanvasGraphAnnotation.from_dict(open_canvas_graph_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


