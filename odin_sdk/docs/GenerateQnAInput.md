# GenerateQnAInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_key** | **str** |  | 
**snippet_type** | **str** |  | [optional] [default to 'faq']

## Example

```python
from odin_sdk.models.generate_qn_a_input import GenerateQnAInput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateQnAInput from a JSON string
generate_qn_a_input_instance = GenerateQnAInput.from_json(json)
# print the JSON string representation of the object
print(GenerateQnAInput.to_json())

# convert the object into a dict
generate_qn_a_input_dict = generate_qn_a_input_instance.to_dict()
# create an instance of GenerateQnAInput from a dict
generate_qn_a_input_from_dict = GenerateQnAInput.from_dict(generate_qn_a_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


