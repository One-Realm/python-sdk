# GetAllPersonalitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalities** | [**List[SystemPromptData]**](SystemPromptData.md) |  | 

## Example

```python
from odin_sdk.models.get_all_personalities_response import GetAllPersonalitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPersonalitiesResponse from a JSON string
get_all_personalities_response_instance = GetAllPersonalitiesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllPersonalitiesResponse.to_json())

# convert the object into a dict
get_all_personalities_response_dict = get_all_personalities_response_instance.to_dict()
# create an instance of GetAllPersonalitiesResponse from a dict
get_all_personalities_response_from_dict = GetAllPersonalitiesResponse.from_dict(get_all_personalities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


