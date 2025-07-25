# ExtensiveSearchRequest

Request model for extensive search job submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_response** | **object** | Previous response containing products and matches | 
**user_prompt** | **str** | User query/prompt for product search | 
**provider** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.extensive_search_request import ExtensiveSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensiveSearchRequest from a JSON string
extensive_search_request_instance = ExtensiveSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ExtensiveSearchRequest.to_json())

# convert the object into a dict
extensive_search_request_dict = extensive_search_request_instance.to_dict()
# create an instance of ExtensiveSearchRequest from a dict
extensive_search_request_from_dict = ExtensiveSearchRequest.from_dict(extensive_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


