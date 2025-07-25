# BodyFindProspeoDataToolsProspeoPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**req** | [**ProspeoRequest**](ProspeoRequest.md) |  | 
**domain_search** | [**DomainSearchRequest**](DomainSearchRequest.md) |  | [optional] 
**email_finder** | [**EmailFinderRequest**](EmailFinderRequest.md) |  | [optional] 
**linkedin_email_finder** | [**LinkedInEmailFinderRequest**](LinkedInEmailFinderRequest.md) |  | [optional] 
**email_verifier** | [**EmailVerifierRequest**](EmailVerifierRequest.md) |  | [optional] 

## Example

```python
from odin_sdk.models.body_find_prospeo_data_tools_prospeo_post import BodyFindProspeoDataToolsProspeoPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyFindProspeoDataToolsProspeoPost from a JSON string
body_find_prospeo_data_tools_prospeo_post_instance = BodyFindProspeoDataToolsProspeoPost.from_json(json)
# print the JSON string representation of the object
print(BodyFindProspeoDataToolsProspeoPost.to_json())

# convert the object into a dict
body_find_prospeo_data_tools_prospeo_post_dict = body_find_prospeo_data_tools_prospeo_post_instance.to_dict()
# create an instance of BodyFindProspeoDataToolsProspeoPost from a dict
body_find_prospeo_data_tools_prospeo_post_from_dict = BodyFindProspeoDataToolsProspeoPost.from_dict(body_find_prospeo_data_tools_prospeo_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


