# Queries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[StoredQuery]**](StoredQuery.md) |  | 

## Example

```python
from odin_sdk.models.queries import Queries

# TODO update the JSON string below
json = "{}"
# create an instance of Queries from a JSON string
queries_instance = Queries.from_json(json)
# print the JSON string representation of the object
print(Queries.to_json())

# convert the object into a dict
queries_dict = queries_instance.to_dict()
# create an instance of Queries from a dict
queries_from_dict = Queries.from_dict(queries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


