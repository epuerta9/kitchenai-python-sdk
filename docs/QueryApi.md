# kitchenai_python_sdk.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_api_query_query**](QueryApi.md#kitchenai_core_api_query_query) | **POST** /api/v1/query/{label} | Query


# **kitchenai_core_api_query_query**
> QueryResponseSchema kitchenai_core_api_query_query(label, query_schema)

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
    api_instance = kitchenai_python_sdk.QueryApi(api_client)
    label = 'label_example' # str | 
    query_schema = kitchenai_python_sdk.QuerySchema() # QuerySchema | 

    try:
        # Query
        api_response = api_instance.kitchenai_core_api_query_query(label, query_schema)
        print("The response of QueryApi->kitchenai_core_api_query_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->kitchenai_core_api_query_query: %s\n" % e)
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

