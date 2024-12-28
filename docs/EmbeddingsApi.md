# kitchenai_python_sdk.EmbeddingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_api_embedding_embed_create**](EmbeddingsApi.md#kitchenai_core_api_embedding_embed_create) | **POST** /api/v1/embeddings/ | Embed Create
[**kitchenai_core_api_embedding_embed_delete**](EmbeddingsApi.md#kitchenai_core_api_embedding_embed_delete) | **DELETE** /api/v1/embeddings/{pk} | Embed Delete
[**kitchenai_core_api_embedding_embed_get**](EmbeddingsApi.md#kitchenai_core_api_embedding_embed_get) | **GET** /api/v1/embeddings/{pk} | Embed Get
[**kitchenai_core_api_embedding_embeds_get**](EmbeddingsApi.md#kitchenai_core_api_embedding_embeds_get) | **GET** /api/v1/embeddings/ | Embeds Get


# **kitchenai_core_api_embedding_embed_create**
> EmbedObjectResponse kitchenai_core_api_embedding_embed_create(embed_schema)

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
    api_instance = kitchenai_python_sdk.EmbeddingsApi(api_client)
    embed_schema = kitchenai_python_sdk.EmbedSchema() # EmbedSchema | 

    try:
        # Embed Create
        api_response = api_instance.kitchenai_core_api_embedding_embed_create(embed_schema)
        print("The response of EmbeddingsApi->kitchenai_core_api_embedding_embed_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->kitchenai_core_api_embedding_embed_create: %s\n" % e)
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

# **kitchenai_core_api_embedding_embed_delete**
> kitchenai_core_api_embedding_embed_delete(pk)

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
    api_instance = kitchenai_python_sdk.EmbeddingsApi(api_client)
    pk = 56 # int | 

    try:
        # Embed Delete
        api_instance.kitchenai_core_api_embedding_embed_delete(pk)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->kitchenai_core_api_embedding_embed_delete: %s\n" % e)
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

# **kitchenai_core_api_embedding_embed_get**
> EmbedObjectResponse kitchenai_core_api_embedding_embed_get(pk)

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
    api_instance = kitchenai_python_sdk.EmbeddingsApi(api_client)
    pk = 56 # int | 

    try:
        # Embed Get
        api_response = api_instance.kitchenai_core_api_embedding_embed_get(pk)
        print("The response of EmbeddingsApi->kitchenai_core_api_embedding_embed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->kitchenai_core_api_embedding_embed_get: %s\n" % e)
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

# **kitchenai_core_api_embedding_embeds_get**
> List[EmbedObjectResponse] kitchenai_core_api_embedding_embeds_get()

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
    api_instance = kitchenai_python_sdk.EmbeddingsApi(api_client)

    try:
        # Embeds Get
        api_response = api_instance.kitchenai_core_api_embedding_embeds_get()
        print("The response of EmbeddingsApi->kitchenai_core_api_embedding_embeds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->kitchenai_core_api_embedding_embeds_get: %s\n" % e)
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

