# CreditAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[Action]**](Action.md) |  | 

## Example

```python
from odin_sdk.models.credit_analytics_response import CreditAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAnalyticsResponse from a JSON string
credit_analytics_response_instance = CreditAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(CreditAnalyticsResponse.to_json())

# convert the object into a dict
credit_analytics_response_dict = credit_analytics_response_instance.to_dict()
# create an instance of CreditAnalyticsResponse from a dict
credit_analytics_response_from_dict = CreditAnalyticsResponse.from_dict(credit_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


