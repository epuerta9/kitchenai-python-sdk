# kitchenai_python_sdk.PlaygroundApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_playground_app_router_default**](PlaygroundApi.md#kitchenai_playground_app_router_default) | **GET** /api/playground/v1/health | Default


# **kitchenai_playground_app_router_default**
> kitchenai_playground_app_router_default()

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
    api_instance = kitchenai_python_sdk.PlaygroundApi(api_client)

    try:
        # Default
        api_instance.kitchenai_playground_app_router_default()
    except Exception as e:
        print("Exception when calling PlaygroundApi->kitchenai_playground_app_router_default: %s\n" % e)
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

