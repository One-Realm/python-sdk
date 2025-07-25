# SingleTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 

## Example

```python
from odin_sdk.models.single_tag_request import SingleTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SingleTagRequest from a JSON string
single_tag_request_instance = SingleTagRequest.from_json(json)
# print the JSON string representation of the object
print(SingleTagRequest.to_json())

# convert the object into a dict
single_tag_request_dict = single_tag_request_instance.to_dict()
# create an instance of SingleTagRequest from a dict
single_tag_request_from_dict = SingleTagRequest.from_dict(single_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


