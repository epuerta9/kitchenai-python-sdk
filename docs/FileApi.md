# kitchenai_python_sdk.FileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_api_file_file_delete**](FileApi.md#kitchenai_core_api_file_file_delete) | **DELETE** /api/v1/file/{pk} | File Delete
[**kitchenai_core_api_file_file_get**](FileApi.md#kitchenai_core_api_file_file_get) | **GET** /api/v1/file/{pk} | File Get
[**kitchenai_core_api_file_file_upload**](FileApi.md#kitchenai_core_api_file_file_upload) | **POST** /api/v1/file/ | File Upload
[**kitchenai_core_api_file_files_get**](FileApi.md#kitchenai_core_api_file_files_get) | **GET** /api/v1/file/ | Files Get


# **kitchenai_core_api_file_file_delete**
> kitchenai_core_api_file_file_delete(pk)

File Delete

delete a file

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kitchenai_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kitchenai_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kitchenai_python_sdk.FileApi(api_client)
    pk = 56 # int | 

    try:
        # File Delete
        api_instance.kitchenai_core_api_file_file_delete(pk)
    except Exception as e:
        print("Exception when calling FileApi->kitchenai_core_api_file_file_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kitchenai_core_api_file_file_get**
> FileObjectResponse kitchenai_core_api_file_file_get(pk)

File Get

get a file

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.file_object_response import FileObjectResponse
from kitchenai_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kitchenai_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kitchenai_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kitchenai_python_sdk.FileApi(api_client)
    pk = 56 # int | 

    try:
        # File Get
        api_response = api_instance.kitchenai_core_api_file_file_get(pk)
        print("The response of FileApi->kitchenai_core_api_file_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->kitchenai_core_api_file_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**|  | 

### Return type

[**FileObjectResponse**](FileObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kitchenai_core_api_file_file_upload**
> FileObjectResponse kitchenai_core_api_file_file_upload(file, data)

File Upload

main entry for any file upload. Will upload via django storage and emit signals to any listeners

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.file_object_response import FileObjectResponse
from kitchenai_python_sdk.models.file_object_schema import FileObjectSchema
from kitchenai_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kitchenai_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kitchenai_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kitchenai_python_sdk.FileApi(api_client)
    file = None # bytearray | 
    data = kitchenai_python_sdk.FileObjectSchema() # FileObjectSchema | 

    try:
        # File Upload
        api_response = api_instance.kitchenai_core_api_file_file_upload(file, data)
        print("The response of FileApi->kitchenai_core_api_file_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->kitchenai_core_api_file_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **data** | [**FileObjectSchema**](FileObjectSchema.md)|  | 

### Return type

[**FileObjectResponse**](FileObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kitchenai_core_api_file_files_get**
> List[FileObjectResponse] kitchenai_core_api_file_files_get()

Files Get

get all files

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.file_object_response import FileObjectResponse
from kitchenai_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kitchenai_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kitchenai_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kitchenai_python_sdk.FileApi(api_client)

    try:
        # Files Get
        api_response = api_instance.kitchenai_core_api_file_files_get()
        print("The response of FileApi->kitchenai_core_api_file_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->kitchenai_core_api_file_files_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FileObjectResponse]**](FileObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

