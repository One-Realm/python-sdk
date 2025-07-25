# ExtractDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**job_id** | **str** |  | 

## Example

```python
from odin_sdk.models.extract_data_response import ExtractDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractDataResponse from a JSON string
extract_data_response_instance = ExtractDataResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractDataResponse.to_json())

# convert the object into a dict
extract_data_response_dict = extract_data_response_instance.to_dict()
# create an instance of ExtractDataResponse from a dict
extract_data_response_from_dict = ExtractDataResponse.from_dict(extract_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


