# kitchenai-python-sdk
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

# Generate 

`docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate     -i /local/openapi.json     -g python     -o /local/     -p packageName=kitchenai_python_sdk`

change ownership 

`sudo chown -R epuerta.epuerta .`

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kitchenai_python_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kitchenai_python_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    label = 'label_example' # str | 
    query_schema = kitchenai_python_sdk.QuerySchema() # QuerySchema | 

    try:
        # Agent Handler
        api_instance.kitchenai_contrib_kitchenai_sdk_kitchenai_agent_handler(label, query_schema)
    except ApiException as e:
        print("Exception when calling DefaultApi->kitchenai_contrib_kitchenai_sdk_kitchenai_agent_handler: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**kitchenai_contrib_kitchenai_sdk_kitchenai_agent_handler**](docs/DefaultApi.md#kitchenai_contrib_kitchenai_sdk_kitchenai_agent_handler) | **POST** /api/default/agent/{label} | Agent Handler
*DefaultApi* | [**kitchenai_contrib_kitchenai_sdk_kitchenai_query_handler**](docs/DefaultApi.md#kitchenai_contrib_kitchenai_sdk_kitchenai_query_handler) | **POST** /api/default/query/{label} | Query Handler
*DefaultApi* | [**kitchenai_core_api_default**](docs/DefaultApi.md#kitchenai_core_api_default) | **GET** /api/core/health | Default
*DefaultApi* | [**kitchenai_core_api_embed_create**](docs/DefaultApi.md#kitchenai_core_api_embed_create) | **POST** /api/core/embed | Embed Create
*DefaultApi* | [**kitchenai_core_api_embed_delete**](docs/DefaultApi.md#kitchenai_core_api_embed_delete) | **DELETE** /api/core/embed/{pk} | Embed Delete
*DefaultApi* | [**kitchenai_core_api_embed_get**](docs/DefaultApi.md#kitchenai_core_api_embed_get) | **GET** /api/core/embed/{pk} | Embed Get
*DefaultApi* | [**kitchenai_core_api_embeds_get**](docs/DefaultApi.md#kitchenai_core_api_embeds_get) | **GET** /api/core/embed | Embeds Get
*DefaultApi* | [**kitchenai_core_api_file_delete**](docs/DefaultApi.md#kitchenai_core_api_file_delete) | **DELETE** /api/core/file/{pk} | File Delete
*DefaultApi* | [**kitchenai_core_api_file_get**](docs/DefaultApi.md#kitchenai_core_api_file_get) | **GET** /api/core/file/{pk} | File Get
*DefaultApi* | [**kitchenai_core_api_file_upload**](docs/DefaultApi.md#kitchenai_core_api_file_upload) | **POST** /api/core/file | File Upload
*DefaultApi* | [**kitchenai_core_api_files_get**](docs/DefaultApi.md#kitchenai_core_api_files_get) | **GET** /api/core/file | Files Get
*DefaultApi* | [**kitchenai_core_api_upload_notebook**](docs/DefaultApi.md#kitchenai_core_api_upload_notebook) | **POST** /api/core/module/upload | Upload Notebook


## Documentation For Models

 - [EmbedObjectResponse](docs/EmbedObjectResponse.md)
 - [EmbedSchema](docs/EmbedSchema.md)
 - [FileObjectResponse](docs/FileObjectResponse.md)
 - [FileObjectSchema](docs/FileObjectSchema.md)
 - [QuerySchema](docs/QuerySchema.md)
 - [UploadModuleInput](docs/UploadModuleInput.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




