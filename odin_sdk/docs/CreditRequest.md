# CreditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** | The IDs of the projects to fetch credit data for. | 
**date_ranges** | [**List[MonthYear]**](MonthYear.md) | The date ranges to fetch credit data for. | 

## Example

```python
from odin_sdk.models.credit_request import CreditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditRequest from a JSON string
credit_request_instance = CreditRequest.from_json(json)
# print the JSON string representation of the object
print(CreditRequest.to_json())

# convert the object into a dict
credit_request_dict = credit_request_instance.to_dict()
# create an instance of CreditRequest from a dict
credit_request_from_dict = CreditRequest.from_dict(credit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


