# FileObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**ingest_label** | **str** |  | 
**metadata** | **Dict[str, str]** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.file_object_response import FileObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileObjectResponse from a JSON string
file_object_response_instance = FileObjectResponse.from_json(json)
# print the JSON string representation of the object
print(FileObjectResponse.to_json())

# convert the object into a dict
file_object_response_dict = file_object_response_instance.to_dict()
# create an instance of FileObjectResponse from a dict
file_object_response_from_dict = FileObjectResponse.from_dict(file_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


