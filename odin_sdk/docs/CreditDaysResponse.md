# CreditDaysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits_last_7_days** | **int** |  | 
**credits_last_30_days** | **int** |  | 
**credits_all_time** | **int** |  | 

## Example

```python
from odin_sdk.models.credit_days_response import CreditDaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDaysResponse from a JSON string
credit_days_response_instance = CreditDaysResponse.from_json(json)
# print the JSON string representation of the object
print(CreditDaysResponse.to_json())

# convert the object into a dict
credit_days_response_dict = credit_days_response_instance.to_dict()
# create an instance of CreditDaysResponse from a dict
credit_days_response_from_dict = CreditDaysResponse.from_dict(credit_days_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


