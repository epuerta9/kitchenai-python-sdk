# QueryResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**retrieval_context** | **List[str]** |  | [optional] 
**stream_gen** | [**AnyOf**](AnyOf.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**kitchenai_metadata** | [**KitchenAIMetadata**](KitchenAIMetadata.md) |  | [optional] 

## Example

```python
from kitchenai_python_sdk.models.query_response_schema import QueryResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResponseSchema from a JSON string
query_response_schema_instance = QueryResponseSchema.from_json(json)
# print the JSON string representation of the object
print(QueryResponseSchema.to_json())

# convert the object into a dict
query_response_schema_dict = query_response_schema_instance.to_dict()
# create an instance of QueryResponseSchema from a dict
query_response_schema_from_dict = QueryResponseSchema.from_dict(query_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


