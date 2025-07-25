# StockDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**metrics** | **List[str]** |  | 

## Example

```python
from odin_sdk.models.stock_data_request import StockDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockDataRequest from a JSON string
stock_data_request_instance = StockDataRequest.from_json(json)
# print the JSON string representation of the object
print(StockDataRequest.to_json())

# convert the object into a dict
stock_data_request_dict = stock_data_request_instance.to_dict()
# create an instance of StockDataRequest from a dict
stock_data_request_from_dict = StockDataRequest.from_dict(stock_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


