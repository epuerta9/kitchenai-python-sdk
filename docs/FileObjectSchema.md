# FileObjectSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**ingest_label** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.file_object_schema import FileObjectSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FileObjectSchema from a JSON string
file_object_schema_instance = FileObjectSchema.from_json(json)
# print the JSON string representation of the object
print(FileObjectSchema.to_json())

# convert the object into a dict
file_object_schema_dict = file_object_schema_instance.to_dict()
# create an instance of FileObjectSchema from a dict
file_object_schema_from_dict = FileObjectSchema.from_dict(file_object_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


