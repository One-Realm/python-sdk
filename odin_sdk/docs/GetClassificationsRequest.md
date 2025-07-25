# GetClassificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 

## Example

```python
from odin_sdk.models.get_classifications_request import GetClassificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetClassificationsRequest from a JSON string
get_classifications_request_instance = GetClassificationsRequest.from_json(json)
# print the JSON string representation of the object
print(GetClassificationsRequest.to_json())

# convert the object into a dict
get_classifications_request_dict = get_classifications_request_instance.to_dict()
# create an instance of GetClassificationsRequest from a dict
get_classifications_request_from_dict = GetClassificationsRequest.from_dict(get_classifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


