# coding: utf-8

"""
    The ParaBank REST API

    This API provides access to various ParaBank internal operations  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: webadmin@parabank.parasoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.database_api import DatabaseApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDatabaseApi(unittest.TestCase):
    """DatabaseApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.database_api.DatabaseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clean_db1(self):
        """Test case for clean_db1

        Clean the Database  # noqa: E501
        """
        pass

    def test_initialize_db1(self):
        """Test case for initialize_db1

        Initialize the Database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()