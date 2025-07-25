# PaginatedAuditLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[AuditLog]**](AuditLog.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from odin_sdk.models.paginated_audit_logs_response import PaginatedAuditLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuditLogsResponse from a JSON string
paginated_audit_logs_response_instance = PaginatedAuditLogsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuditLogsResponse.to_json())

# convert the object into a dict
paginated_audit_logs_response_dict = paginated_audit_logs_response_instance.to_dict()
# create an instance of PaginatedAuditLogsResponse from a dict
paginated_audit_logs_response_from_dict = PaginatedAuditLogsResponse.from_dict(paginated_audit_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


