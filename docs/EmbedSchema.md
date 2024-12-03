# EmbedSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**ingest_label** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.embed_schema import EmbedSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmbedSchema from a JSON string
embed_schema_instance = EmbedSchema.from_json(json)
# print the JSON string representation of the object
print(EmbedSchema.to_json())

# convert the object into a dict
embed_schema_dict = embed_schema_instance.to_dict()
# create an instance of EmbedSchema from a dict
embed_schema_from_dict = EmbedSchema.from_dict(embed_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


