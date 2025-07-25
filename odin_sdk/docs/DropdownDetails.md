# DropdownDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the dropdown option. | 
**value** | **str** | The value of the dropdown option. | 

## Example

```python
from odin_sdk.models.dropdown_details import DropdownDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DropdownDetails from a JSON string
dropdown_details_instance = DropdownDetails.from_json(json)
# print the JSON string representation of the object
print(DropdownDetails.to_json())

# convert the object into a dict
dropdown_details_dict = dropdown_details_instance.to_dict()
# create an instance of DropdownDetails from a dict
dropdown_details_from_dict = DropdownDetails.from_dict(dropdown_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


