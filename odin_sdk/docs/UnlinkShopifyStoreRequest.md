# UnlinkShopifyStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**shop_name** | **str** |  | 

## Example

```python
from odin_sdk.models.unlink_shopify_store_request import UnlinkShopifyStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkShopifyStoreRequest from a JSON string
unlink_shopify_store_request_instance = UnlinkShopifyStoreRequest.from_json(json)
# print the JSON string representation of the object
print(UnlinkShopifyStoreRequest.to_json())

# convert the object into a dict
unlink_shopify_store_request_dict = unlink_shopify_store_request_instance.to_dict()
# create an instance of UnlinkShopifyStoreRequest from a dict
unlink_shopify_store_request_from_dict = UnlinkShopifyStoreRequest.from_dict(unlink_shopify_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


