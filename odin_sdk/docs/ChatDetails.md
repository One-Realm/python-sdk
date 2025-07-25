# ChatDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**document_keys** | **List[str]** |  | [optional] 
**created_by** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **float** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.chat_details import ChatDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ChatDetails from a JSON string
chat_details_instance = ChatDetails.from_json(json)
# print the JSON string representation of the object
print(ChatDetails.to_json())

# convert the object into a dict
chat_details_dict = chat_details_instance.to_dict()
# create an instance of ChatDetails from a dict
chat_details_from_dict = ChatDetails.from_dict(chat_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


