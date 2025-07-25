# PublishResponse

Response model for publishing a script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**version** | **str** |  | 
**published_at** | **datetime** |  | 

## Example

```python
from odin_sdk.models.publish_response import PublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResponse from a JSON string
publish_response_instance = PublishResponse.from_json(json)
# print the JSON string representation of the object
print(PublishResponse.to_json())

# convert the object into a dict
publish_response_dict = publish_response_instance.to_dict()
# create an instance of PublishResponse from a dict
publish_response_from_dict = PublishResponse.from_dict(publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


