# LinkedInSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linkedin_profiles** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.linked_in_search_response import LinkedInSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedInSearchResponse from a JSON string
linked_in_search_response_instance = LinkedInSearchResponse.from_json(json)
# print the JSON string representation of the object
print(LinkedInSearchResponse.to_json())

# convert the object into a dict
linked_in_search_response_dict = linked_in_search_response_instance.to_dict()
# create an instance of LinkedInSearchResponse from a dict
linked_in_search_response_from_dict = LinkedInSearchResponse.from_dict(linked_in_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


