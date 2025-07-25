# EmailCreatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Project ID in which to run the email creator. | 
**sender** | **str** | Sender of the email. | 
**content_instructions** | **List[str]** | Instructions for the content of the email. Provided as an array of strings. | 
**formatting_example** | **str** | Example of the formatting of the email. | 
**generate_html** | **bool** |  | [optional] 
**model_name** | **str** |  | [optional] 
**recipient** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.email_creator_request import EmailCreatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCreatorRequest from a JSON string
email_creator_request_instance = EmailCreatorRequest.from_json(json)
# print the JSON string representation of the object
print(EmailCreatorRequest.to_json())

# convert the object into a dict
email_creator_request_dict = email_creator_request_instance.to_dict()
# create an instance of EmailCreatorRequest from a dict
email_creator_request_from_dict = EmailCreatorRequest.from_dict(email_creator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


