# UpdateUserCreditLimitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**credit_limit** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.update_user_credit_limit_request import UpdateUserCreditLimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserCreditLimitRequest from a JSON string
update_user_credit_limit_request_instance = UpdateUserCreditLimitRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserCreditLimitRequest.to_json())

# convert the object into a dict
update_user_credit_limit_request_dict = update_user_credit_limit_request_instance.to_dict()
# create an instance of UpdateUserCreditLimitRequest from a dict
update_user_credit_limit_request_from_dict = UpdateUserCreditLimitRequest.from_dict(update_user_credit_limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


