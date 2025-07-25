# PurchaseSeatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_price** | **float** |  | 

## Example

```python
from odin_sdk.models.purchase_seats_response import PurchaseSeatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseSeatsResponse from a JSON string
purchase_seats_response_instance = PurchaseSeatsResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseSeatsResponse.to_json())

# convert the object into a dict
purchase_seats_response_dict = purchase_seats_response_instance.to_dict()
# create an instance of PurchaseSeatsResponse from a dict
purchase_seats_response_from_dict = PurchaseSeatsResponse.from_dict(purchase_seats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


