# KitchenAIAppSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | 
**query_handlers** | **List[str]** |  | 
**agent_handlers** | **List[str]** |  | 
**embed_tasks** | **List[str]** |  | 
**embed_delete_tasks** | **List[str]** |  | 
**storage_tasks** | **List[str]** |  | 
**storage_delete_tasks** | **List[str]** |  | 
**storage_create_hooks** | **List[str]** |  | 
**storage_delete_hooks** | **List[str]** |  | 

## Example

```python
from kitchenai_python_sdk.models.kitchen_ai_app_schema import KitchenAIAppSchema

# TODO update the JSON string below
json = "{}"
# create an instance of KitchenAIAppSchema from a JSON string
kitchen_ai_app_schema_instance = KitchenAIAppSchema.from_json(json)
# print the JSON string representation of the object
print(KitchenAIAppSchema.to_json())

# convert the object into a dict
kitchen_ai_app_schema_dict = kitchen_ai_app_schema_instance.to_dict()
# create an instance of KitchenAIAppSchema from a dict
kitchen_ai_app_schema_from_dict = KitchenAIAppSchema.from_dict(kitchen_ai_app_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


