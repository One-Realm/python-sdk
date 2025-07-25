# ApplyStyleGuideRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**text** | **str** |  | 
**use_llm** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.apply_style_guide_request import ApplyStyleGuideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyStyleGuideRequest from a JSON string
apply_style_guide_request_instance = ApplyStyleGuideRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyStyleGuideRequest.to_json())

# convert the object into a dict
apply_style_guide_request_dict = apply_style_guide_request_instance.to_dict()
# create an instance of ApplyStyleGuideRequest from a dict
apply_style_guide_request_from_dict = ApplyStyleGuideRequest.from_dict(apply_style_guide_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


