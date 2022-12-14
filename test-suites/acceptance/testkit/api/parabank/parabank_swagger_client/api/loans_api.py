# coding: utf-8

"""
    The ParaBank REST API

    This API provides access to various ParaBank internal operations  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: webadmin@parabank.parasoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LoansApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def request_loan1(self, customer_id, amount, down_payment, from_account_id, **kwargs):  # noqa: E501
        """Request a loan  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_loan1(customer_id, amount, down_payment, from_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int customer_id: Customer's id (required)
        :param float amount: Amount (required)
        :param float down_payment: Downpayment for the loan (required)
        :param int from_account_id: Customer funds source account (required)
        :return: LoanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_loan1_with_http_info(customer_id, amount, down_payment, from_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.request_loan1_with_http_info(customer_id, amount, down_payment, from_account_id, **kwargs)  # noqa: E501
            return data

    def request_loan1_with_http_info(self, customer_id, amount, down_payment, from_account_id, **kwargs):  # noqa: E501
        """Request a loan  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_loan1_with_http_info(customer_id, amount, down_payment, from_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int customer_id: Customer's id (required)
        :param float amount: Amount (required)
        :param float down_payment: Downpayment for the loan (required)
        :param int from_account_id: Customer funds source account (required)
        :return: LoanResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'amount', 'down_payment', 'from_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_loan1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if self.api_client.client_side_validation and ('customer_id' not in params or
                                                       params['customer_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `customer_id` when calling `request_loan1`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if self.api_client.client_side_validation and ('amount' not in params or
                                                       params['amount'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `amount` when calling `request_loan1`")  # noqa: E501
        # verify the required parameter 'down_payment' is set
        if self.api_client.client_side_validation and ('down_payment' not in params or
                                                       params['down_payment'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `down_payment` when calling `request_loan1`")  # noqa: E501
        # verify the required parameter 'from_account_id' is set
        if self.api_client.client_side_validation and ('from_account_id' not in params or
                                                       params['from_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `from_account_id` when calling `request_loan1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'customer_id' in params:
            query_params.append(('customerId', params['customer_id']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'down_payment' in params:
            query_params.append(('downPayment', params['down_payment']))  # noqa: E501
        if 'from_account_id' in params:
            query_params.append(('fromAccountId', params['from_account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/requestLoan', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LoanResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
