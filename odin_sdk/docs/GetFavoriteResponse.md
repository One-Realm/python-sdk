# GetFavoriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.get_favorite_response import GetFavoriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFavoriteResponse from a JSON string
get_favorite_response_instance = GetFavoriteResponse.from_json(json)
# print the JSON string representation of the object
print(GetFavoriteResponse.to_json())

# convert the object into a dict
get_favorite_response_dict = get_favorite_response_instance.to_dict()
# create an instance of GetFavoriteResponse from a dict
get_favorite_response_from_dict = GetFavoriteResponse.from_dict(get_favorite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


