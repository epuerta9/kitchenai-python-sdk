# QuerySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**stream** | **bool** |  | [optional] [default to False]
**stream_id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from kitchenai_python_sdk.models.query_schema import QuerySchema

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySchema from a JSON string
query_schema_instance = QuerySchema.from_json(json)
# print the JSON string representation of the object
print(QuerySchema.to_json())

# convert the object into a dict
query_schema_dict = query_schema_instance.to_dict()
# create an instance of QuerySchema from a dict
query_schema_from_dict = QuerySchema.from_dict(query_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


