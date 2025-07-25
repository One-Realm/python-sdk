# FetchDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 

## Example

```python
from odin_sdk.models.fetch_data_response import FetchDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDataResponse from a JSON string
fetch_data_response_instance = FetchDataResponse.from_json(json)
# print the JSON string representation of the object
print(FetchDataResponse.to_json())

# convert the object into a dict
fetch_data_response_dict = fetch_data_response_instance.to_dict()
# create an instance of FetchDataResponse from a dict
fetch_data_response_from_dict = FetchDataResponse.from_dict(fetch_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


