# EmailCreatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** | Output of the email creator. | 

## Example

```python
from odin_sdk.models.email_creator_response import EmailCreatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCreatorResponse from a JSON string
email_creator_response_instance = EmailCreatorResponse.from_json(json)
# print the JSON string representation of the object
print(EmailCreatorResponse.to_json())

# convert the object into a dict
email_creator_response_dict = email_creator_response_instance.to_dict()
# create an instance of EmailCreatorResponse from a dict
email_creator_response_from_dict = EmailCreatorResponse.from_dict(email_creator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


