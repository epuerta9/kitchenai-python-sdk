# kitchenai_python_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_api_agent**](DefaultApi.md#kitchenai_core_api_agent) | **POST** /api/core/agent/{label} | Agent
[**kitchenai_core_api_default**](DefaultApi.md#kitchenai_core_api_default) | **GET** /api/core/health | Default
[**kitchenai_core_api_embed_create**](DefaultApi.md#kitchenai_core_api_embed_create) | **POST** /api/core/embed | Embed Create
[**kitchenai_core_api_embed_delete**](DefaultApi.md#kitchenai_core_api_embed_delete) | **DELETE** /api/core/embed/{pk} | Embed Delete
[**kitchenai_core_api_embed_get**](DefaultApi.md#kitchenai_core_api_embed_get) | **GET** /api/core/embed/{pk} | Embed Get
[**kitchenai_core_api_embeds_get**](DefaultApi.md#kitchenai_core_api_embeds_get) | **GET** /api/core/embed | Embeds Get
[**kitchenai_core_api_file_delete**](DefaultApi.md#kitchenai_core_api_file_delete) | **DELETE** /api/core/file/{pk} | File Delete
[**kitchenai_core_api_file_get**](DefaultApi.md#kitchenai_core_api_file_get) | **GET** /api/core/file/{pk} | File Get
[**kitchenai_core_api_file_upload**](DefaultApi.md#kitchenai_core_api_file_upload) | **POST** /api/core/file | File Upload
[**kitchenai_core_api_files_get**](DefaultApi.md#kitchenai_core_api_files_get) | **GET** /api/core/file | Files Get
[**kitchenai_core_api_labels**](DefaultApi.md#kitchenai_core_api_labels) | **GET** /api/core/labels | Labels
[**kitchenai_core_api_query**](DefaultApi.md#kitchenai_core_api_query) | **POST** /api/core/query/{label} | Query


# **kitchenai_core_api_agent**
> AgentResponseSchema kitchenai_core_api_agent(label, query_schema)

Agent

Create a new agent

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.agent_response_schema import AgentResponseSchema
from kitchenai_python_sdk.models.query_schema import QuerySchema
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    label = 'label_example' # str | 
    query_schema = kitchenai_python_sdk.QuerySchema() # QuerySchema | 

    try:
        # Agent
        api_response = api_instance.kitchenai_core_api_agent(label, query_schema)
        print("The response of DefaultApi->kitchenai_core_api_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**|  | 
 **query_schema** | [**QuerySchema**](QuerySchema.md)|  | 

### Return type

[**AgentResponseSchema**](AgentResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kitchenai_core_api_default**
> kitchenai_core_api_default()

Default

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)

    try:
        # Default
        api_instance.kitchenai_core_api_default()
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_default: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **kitchenai_core_api_embed_create**
> EmbedObjectResponse kitchenai_core_api_embed_create(embed_schema)

Embed Create

Create a new embed from text

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.embed_object_response import EmbedObjectResponse
from kitchenai_python_sdk.models.embed_schema import EmbedSchema
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    embed_schema = kitchenai_python_sdk.EmbedSchema() # EmbedSchema | 

    try:
        # Embed Create
        api_response = api_instance.kitchenai_core_api_embed_create(embed_schema)
        print("The response of DefaultApi->kitchenai_core_api_embed_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_embed_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embed_schema** | [**EmbedSchema**](EmbedSchema.md)|  | 

### Return type

[**EmbedObjectResponse**](EmbedObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kitchenai_core_api_embed_delete**
> kitchenai_core_api_embed_delete(pk)

Embed Delete

Delete an embed

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    pk = 56 # int | 

    try:
        # Embed Delete
        api_instance.kitchenai_core_api_embed_delete(pk)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_embed_delete: %s\n" % e)
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

# **kitchenai_core_api_embed_get**
> EmbedObjectResponse kitchenai_core_api_embed_get(pk)

Embed Get

Get an embed

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.embed_object_response import EmbedObjectResponse
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    pk = 56 # int | 

    try:
        # Embed Get
        api_response = api_instance.kitchenai_core_api_embed_get(pk)
        print("The response of DefaultApi->kitchenai_core_api_embed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_embed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk** | **int**|  | 

### Return type

[**EmbedObjectResponse**](EmbedObjectResponse.md)

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

# **kitchenai_core_api_embeds_get**
> List[EmbedObjectResponse] kitchenai_core_api_embeds_get()

Embeds Get

Get all embeds

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.embed_object_response import EmbedObjectResponse
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)

    try:
        # Embeds Get
        api_response = api_instance.kitchenai_core_api_embeds_get()
        print("The response of DefaultApi->kitchenai_core_api_embeds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_embeds_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EmbedObjectResponse]**](EmbedObjectResponse.md)

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

# **kitchenai_core_api_file_delete**
> kitchenai_core_api_file_delete(pk)

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    pk = 56 # int | 

    try:
        # File Delete
        api_instance.kitchenai_core_api_file_delete(pk)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_file_delete: %s\n" % e)
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

# **kitchenai_core_api_file_get**
> FileObjectResponse kitchenai_core_api_file_get(pk)

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    pk = 56 # int | 

    try:
        # File Get
        api_response = api_instance.kitchenai_core_api_file_get(pk)
        print("The response of DefaultApi->kitchenai_core_api_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_file_get: %s\n" % e)
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

# **kitchenai_core_api_file_upload**
> FileObjectResponse kitchenai_core_api_file_upload(file, data)

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    file = None # bytearray | 
    data = kitchenai_python_sdk.FileObjectSchema() # FileObjectSchema | 

    try:
        # File Upload
        api_response = api_instance.kitchenai_core_api_file_upload(file, data)
        print("The response of DefaultApi->kitchenai_core_api_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_file_upload: %s\n" % e)
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

# **kitchenai_core_api_files_get**
> List[FileObjectResponse] kitchenai_core_api_files_get()

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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)

    try:
        # Files Get
        api_response = api_instance.kitchenai_core_api_files_get()
        print("The response of DefaultApi->kitchenai_core_api_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_files_get: %s\n" % e)
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

# **kitchenai_core_api_labels**
> KitchenAIAppSchema kitchenai_core_api_labels()

Labels

Lists all the custom kitchenai labels

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.kitchen_ai_app_schema import KitchenAIAppSchema
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)

    try:
        # Labels
        api_response = api_instance.kitchenai_core_api_labels()
        print("The response of DefaultApi->kitchenai_core_api_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_labels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**KitchenAIAppSchema**](KitchenAIAppSchema.md)

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

# **kitchenai_core_api_query**
> QueryResponseSchema kitchenai_core_api_query(label, query_schema)

Query

Create a new query

### Example


```python
import kitchenai_python_sdk
from kitchenai_python_sdk.models.query_response_schema import QueryResponseSchema
from kitchenai_python_sdk.models.query_schema import QuerySchema
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
    api_instance = kitchenai_python_sdk.DefaultApi(api_client)
    label = 'label_example' # str | 
    query_schema = kitchenai_python_sdk.QuerySchema() # QuerySchema | 

    try:
        # Query
        api_response = api_instance.kitchenai_core_api_query(label, query_schema)
        print("The response of DefaultApi->kitchenai_core_api_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_api_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**|  | 
 **query_schema** | [**QuerySchema**](QuerySchema.md)|  | 

### Return type

[**QueryResponseSchema**](QueryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

