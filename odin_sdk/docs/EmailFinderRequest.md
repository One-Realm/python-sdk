# EmailFinderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**company** | **str** |  | 

## Example

```python
from odin_sdk.models.email_finder_request import EmailFinderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailFinderRequest from a JSON string
email_finder_request_instance = EmailFinderRequest.from_json(json)
# print the JSON string representation of the object
print(EmailFinderRequest.to_json())

# convert the object into a dict
email_finder_request_dict = email_finder_request_instance.to_dict()
# create an instance of EmailFinderRequest from a dict
email_finder_request_from_dict = EmailFinderRequest.from_dict(email_finder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


