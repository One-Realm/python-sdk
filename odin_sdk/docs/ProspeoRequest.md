# ProspeoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_type** | **str** |  | 

## Example

```python
from odin_sdk.models.prospeo_request import ProspeoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProspeoRequest from a JSON string
prospeo_request_instance = ProspeoRequest.from_json(json)
# print the JSON string representation of the object
print(ProspeoRequest.to_json())

# convert the object into a dict
prospeo_request_dict = prospeo_request_instance.to_dict()
# create an instance of ProspeoRequest from a dict
prospeo_request_from_dict = ProspeoRequest.from_dict(prospeo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


