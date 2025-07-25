# DomainSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str** |  | 
**limit** | **int** |  | [optional] [default to 5]
**email_type** | **str** |  | [optional] 
**company_enrichment** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.domain_search_request import DomainSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainSearchRequest from a JSON string
domain_search_request_instance = DomainSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DomainSearchRequest.to_json())

# convert the object into a dict
domain_search_request_dict = domain_search_request_instance.to_dict()
# create an instance of DomainSearchRequest from a dict
domain_search_request_from_dict = DomainSearchRequest.from_dict(domain_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


