# LinkShopifyStoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**success** | **bool** |  | 
**shop_name** | **str** |  | 
**alias** | **str** |  | 

## Example

```python
from odin_sdk.models.link_shopify_store_response import LinkShopifyStoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkShopifyStoreResponse from a JSON string
link_shopify_store_response_instance = LinkShopifyStoreResponse.from_json(json)
# print the JSON string representation of the object
print(LinkShopifyStoreResponse.to_json())

# convert the object into a dict
link_shopify_store_response_dict = link_shopify_store_response_instance.to_dict()
# create an instance of LinkShopifyStoreResponse from a dict
link_shopify_store_response_from_dict = LinkShopifyStoreResponse.from_dict(link_shopify_store_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


