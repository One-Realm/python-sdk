# UsageReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.usage_report_request import UsageReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsageReportRequest from a JSON string
usage_report_request_instance = UsageReportRequest.from_json(json)
# print the JSON string representation of the object
print(UsageReportRequest.to_json())

# convert the object into a dict
usage_report_request_dict = usage_report_request_instance.to_dict()
# create an instance of UsageReportRequest from a dict
usage_report_request_from_dict = UsageReportRequest.from_dict(usage_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


