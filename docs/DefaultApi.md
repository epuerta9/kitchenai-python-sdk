# kitchenai_python_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_router_default**](DefaultApi.md#kitchenai_core_router_default) | **GET** /api/v1/health | Default
[**kitchenai_core_router_labels**](DefaultApi.md#kitchenai_core_router_labels) | **GET** /api/v1/labels | Labels


# **kitchenai_core_router_default**
> kitchenai_core_router_default()

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
        api_instance.kitchenai_core_router_default()
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_router_default: %s\n" % e)
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

# **kitchenai_core_router_labels**
> KitchenAIAppSchema kitchenai_core_router_labels()

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
        api_response = api_instance.kitchenai_core_router_labels()
        print("The response of DefaultApi->kitchenai_core_router_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->kitchenai_core_router_labels: %s\n" % e)
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

