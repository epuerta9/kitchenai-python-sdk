# coding: utf-8

# flake8: noqa

"""
    NinjaAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.embed_object_response import EmbedObjectResponse
from openapi_client.models.embed_schema import EmbedSchema
from openapi_client.models.file_object_response import FileObjectResponse
from openapi_client.models.file_object_schema import FileObjectSchema
from openapi_client.models.query_schema import QuerySchema
from openapi_client.models.upload_module_input import UploadModuleInput