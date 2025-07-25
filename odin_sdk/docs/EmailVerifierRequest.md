# EmailVerifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**email_anon_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.email_verifier_request import EmailVerifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailVerifierRequest from a JSON string
email_verifier_request_instance = EmailVerifierRequest.from_json(json)
# print the JSON string representation of the object
print(EmailVerifierRequest.to_json())

# convert the object into a dict
email_verifier_request_dict = email_verifier_request_instance.to_dict()
# create an instance of EmailVerifierRequest from a dict
email_verifier_request_from_dict = EmailVerifierRequest.from_dict(email_verifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


