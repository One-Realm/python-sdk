# LinkedInEmailFinderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**profile_only** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.linked_in_email_finder_request import LinkedInEmailFinderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedInEmailFinderRequest from a JSON string
linked_in_email_finder_request_instance = LinkedInEmailFinderRequest.from_json(json)
# print the JSON string representation of the object
print(LinkedInEmailFinderRequest.to_json())

# convert the object into a dict
linked_in_email_finder_request_dict = linked_in_email_finder_request_instance.to_dict()
# create an instance of LinkedInEmailFinderRequest from a dict
linked_in_email_finder_request_from_dict = LinkedInEmailFinderRequest.from_dict(linked_in_email_finder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


