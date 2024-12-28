# KitchenAIMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **str** |  | [optional] 
**stream** | **bool** |  | 

## Example

```python
from kitchenai_python_sdk.models.kitchen_ai_metadata import KitchenAIMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KitchenAIMetadata from a JSON string
kitchen_ai_metadata_instance = KitchenAIMetadata.from_json(json)
# print the JSON string representation of the object
print(KitchenAIMetadata.to_json())

# convert the object into a dict
kitchen_ai_metadata_dict = kitchen_ai_metadata_instance.to_dict()
# create an instance of KitchenAIMetadata from a dict
kitchen_ai_metadata_from_dict = KitchenAIMetadata.from_dict(kitchen_ai_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


