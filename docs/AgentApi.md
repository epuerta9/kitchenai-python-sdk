# kitchenai_python_sdk.AgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kitchenai_core_api_agent_agent**](AgentApi.md#kitchenai_core_api_agent_agent) | **POST** /api/v1/agent/{label} | Agent


# **kitchenai_core_api_agent_agent**
> AgentResponseSchema kitchenai_core_api_agent_agent(label, query_schema)

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
    api_instance = kitchenai_python_sdk.AgentApi(api_client)
    label = 'label_example' # str | 
    query_schema = kitchenai_python_sdk.QuerySchema() # QuerySchema | 

    try:
        # Agent
        api_response = api_instance.kitchenai_core_api_agent_agent(label, query_schema)
        print("The response of AgentApi->kitchenai_core_api_agent_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->kitchenai_core_api_agent_agent: %s\n" % e)
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

