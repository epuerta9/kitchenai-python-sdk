# coding: utf-8

"""
    NinjaAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.query_schema import QuerySchema

class TestQuerySchema(unittest.TestCase):
    """QuerySchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuerySchema:
        """Test QuerySchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuerySchema`
        """
        model = QuerySchema()
        if include_optional:
            return QuerySchema(
                query = '',
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return QuerySchema(
                query = '',
        )
        """

    def testQuerySchema(self):
        """Test QuerySchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
