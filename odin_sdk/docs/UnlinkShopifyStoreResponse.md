# UnlinkShopifyStoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from odin_sdk.models.unlink_shopify_store_response import UnlinkShopifyStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkShopifyStoreResponse from a JSON string
unlink_shopify_store_response_instance = UnlinkShopifyStoreResponse.from_json(json)
# print the JSON string representation of the object
print(UnlinkShopifyStoreResponse.to_json())

# convert the object into a dict
unlink_shopify_store_response_dict = unlink_shopify_store_response_instance.to_dict()
# create an instance of UnlinkShopifyStoreResponse from a dict
unlink_shopify_store_response_from_dict = UnlinkShopifyStoreResponse.from_dict(unlink_shopify_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


