# PIICheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**content_keys** | **List[str]** |  | [optional] 
**content** | **str** |  | [optional] 
**scrub_pii** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.pii_check_request import PIICheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PIICheckRequest from a JSON string
pii_check_request_instance = PIICheckRequest.from_json(json)
# print the JSON string representation of the object
print(PIICheckRequest.to_json())

# convert the object into a dict
pii_check_request_dict = pii_check_request_instance.to_dict()
# create an instance of PIICheckRequest from a dict
pii_check_request_from_dict = PIICheckRequest.from_dict(pii_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


