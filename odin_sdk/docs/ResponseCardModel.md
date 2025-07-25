# ResponseCardModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** | The content of the card. | [optional] 

## Example

```python
from odin_sdk.models.response_card_model import ResponseCardModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCardModel from a JSON string
response_card_model_instance = ResponseCardModel.from_json(json)
# print the JSON string representation of the object
print(ResponseCardModel.to_json())

# convert the object into a dict
response_card_model_dict = response_card_model_instance.to_dict()
# create an instance of ResponseCardModel from a dict
response_card_model_from_dict = ResponseCardModel.from_dict(response_card_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


