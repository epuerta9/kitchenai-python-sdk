# EmbedObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**text** | **str** |  | 
**ingest_label** | **str** |  | 
**metadata** | **Dict[str, str]** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.embed_object_response import EmbedObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbedObjectResponse from a JSON string
embed_object_response_instance = EmbedObjectResponse.from_json(json)
# print the JSON string representation of the object
print(EmbedObjectResponse.to_json())

# convert the object into a dict
embed_object_response_dict = embed_object_response_instance.to_dict()
# create an instance of EmbedObjectResponse from a dict
embed_object_response_from_dict = EmbedObjectResponse.from_dict(embed_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


