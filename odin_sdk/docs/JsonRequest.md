# JsonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelJson**](ModelJson.md) |  | 

## Example

```python
from odin_sdk.models.json_request import JsonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRequest from a JSON string
json_request_instance = JsonRequest.from_json(json)
# print the JSON string representation of the object
print(JsonRequest.to_json())

# convert the object into a dict
json_request_dict = json_request_instance.to_dict()
# create an instance of JsonRequest from a dict
json_request_from_dict = JsonRequest.from_dict(json_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


