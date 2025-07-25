# ConvertOldCSVRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**key** | **str** |  | 
**path** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.convert_old_csv_request import ConvertOldCSVRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertOldCSVRequest from a JSON string
convert_old_csv_request_instance = ConvertOldCSVRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertOldCSVRequest.to_json())

# convert the object into a dict
convert_old_csv_request_dict = convert_old_csv_request_instance.to_dict()
# create an instance of ConvertOldCSVRequest from a dict
convert_old_csv_request_from_dict = ConvertOldCSVRequest.from_dict(convert_old_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


