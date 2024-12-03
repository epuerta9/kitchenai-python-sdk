# UploadModuleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** |  | 
**project_path** | **str** |  | 

## Example

```python
from kitchenai_python_sdk.models.upload_module_input import UploadModuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of UploadModuleInput from a JSON string
upload_module_input_instance = UploadModuleInput.from_json(json)
# print the JSON string representation of the object
print(UploadModuleInput.to_json())

# convert the object into a dict
upload_module_input_dict = upload_module_input_instance.to_dict()
# create an instance of UploadModuleInput from a dict
upload_module_input_from_dict = UploadModuleInput.from_dict(upload_module_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


