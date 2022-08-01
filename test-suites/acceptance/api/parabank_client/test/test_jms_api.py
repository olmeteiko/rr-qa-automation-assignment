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
from swagger_client.api.jms_api import JMSApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJMSApi(unittest.TestCase):
    """JMSApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.jms_api.JMSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_shutdown_jms_listener1(self):
        """Test case for shutdown_jms_listener1

        Stop JMS Listener  # noqa: E501
        """
        pass

    def test_startup_jms_listener1(self):
        """Test case for startup_jms_listener1

        Start JMS Listener  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
