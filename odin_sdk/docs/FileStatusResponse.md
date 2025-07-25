# FileStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from odin_sdk.models.file_status_response import FileStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileStatusResponse from a JSON string
file_status_response_instance = FileStatusResponse.from_json(json)
# print the JSON string representation of the object
print(FileStatusResponse.to_json())

# convert the object into a dict
file_status_response_dict = file_status_response_instance.to_dict()
# create an instance of FileStatusResponse from a dict
file_status_response_from_dict = FileStatusResponse.from_dict(file_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


