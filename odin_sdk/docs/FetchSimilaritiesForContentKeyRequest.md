# FetchSimilaritiesForContentKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**document_key** | **str** |  | 
**similarity_threshold** | **float** |  | [optional] [default to 0.5]

## Example

```python
from odin_sdk.models.fetch_similarities_for_content_key_request import FetchSimilaritiesForContentKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchSimilaritiesForContentKeyRequest from a JSON string
fetch_similarities_for_content_key_request_instance = FetchSimilaritiesForContentKeyRequest.from_json(json)
# print the JSON string representation of the object
print(FetchSimilaritiesForContentKeyRequest.to_json())

# convert the object into a dict
fetch_similarities_for_content_key_request_dict = fetch_similarities_for_content_key_request_instance.to_dict()
# create an instance of FetchSimilaritiesForContentKeyRequest from a dict
fetch_similarities_for_content_key_request_from_dict = FetchSimilaritiesForContentKeyRequest.from_dict(fetch_similarities_for_content_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


