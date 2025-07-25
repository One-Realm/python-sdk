# GetKBPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The page number to retrieve | [optional] [default to 1]
**items_per_page** | **int** | The number of items per page | [optional] [default to 30]
**filters** | **object** |  | [optional] 
**name_search** | **str** |  | [optional] 
**content_keys** | **List[str]** |  | [optional] 
**path** | **str** |  | [optional] 
**recursive** | **bool** | Whether to retrieve subfolders | [optional] [default to False]

## Example

```python
from odin_sdk.models.get_kb_page_request import GetKBPageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetKBPageRequest from a JSON string
get_kb_page_request_instance = GetKBPageRequest.from_json(json)
# print the JSON string representation of the object
print(GetKBPageRequest.to_json())

# convert the object into a dict
get_kb_page_request_dict = get_kb_page_request_instance.to_dict()
# create an instance of GetKBPageRequest from a dict
get_kb_page_request_from_dict = GetKBPageRequest.from_dict(get_kb_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


