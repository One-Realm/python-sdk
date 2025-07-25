# GenerateSuggestionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.generate_suggestions_response import GenerateSuggestionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSuggestionsResponse from a JSON string
generate_suggestions_response_instance = GenerateSuggestionsResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateSuggestionsResponse.to_json())

# convert the object into a dict
generate_suggestions_response_dict = generate_suggestions_response_instance.to_dict()
# create an instance of GenerateSuggestionsResponse from a dict
generate_suggestions_response_from_dict = GenerateSuggestionsResponse.from_dict(generate_suggestions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


