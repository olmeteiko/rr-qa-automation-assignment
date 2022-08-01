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


class TransactionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transaction1(self, transaction_id, **kwargs):  # noqa: E501
        """Get the transaction for the id  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction1(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int transaction_id: Unique identifier for the transaction (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transaction1_with_http_info(transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transaction1_with_http_info(transaction_id, **kwargs)  # noqa: E501
            return data

    def get_transaction1_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """Get the transaction for the id  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction1_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int transaction_id: Unique identifier for the transaction (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in params or
                                                       params['transaction_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `transaction_id` when calling `get_transaction1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']  # noqa: E501

        query_params = []

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
            '/transactions/{transactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions1(self, account_id, **kwargs):  # noqa: E501
        """Get the list of Transactions for the account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions1(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions1_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions1_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def get_transactions1_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Get the list of Transactions for the account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions1_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

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
            '/accounts/{accountId}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_by_amount1(self, account_id, amount, **kwargs):  # noqa: E501
        """Create transactions by amount for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_amount1(account_id, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param float amount: Amount (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_by_amount1_with_http_info(account_id, amount, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_by_amount1_with_http_info(account_id, amount, **kwargs)  # noqa: E501
            return data

    def get_transactions_by_amount1_with_http_info(self, account_id, amount, **kwargs):  # noqa: E501
        """Create transactions by amount for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_amount1_with_http_info(account_id, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param float amount: Amount (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_by_amount1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions_by_amount1`")  # noqa: E501
        # verify the required parameter 'amount' is set
        if self.api_client.client_side_validation and ('amount' not in params or
                                                       params['amount'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `amount` when calling `get_transactions_by_amount1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'amount' in params:
            path_params['amount'] = params['amount']  # noqa: E501

        query_params = []

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
            '/accounts/{accountId}/transactions/amount/{amount}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_by_month_and_type1(self, account_id, month, type, **kwargs):  # noqa: E501
        """Fetch transactions by month and type for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_month_and_type1(account_id, month, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str month: Month to use for the search range (required)
        :param str type: Transaction type (CREDIT, DEBIT) (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_by_month_and_type1_with_http_info(account_id, month, type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_by_month_and_type1_with_http_info(account_id, month, type, **kwargs)  # noqa: E501
            return data

    def get_transactions_by_month_and_type1_with_http_info(self, account_id, month, type, **kwargs):  # noqa: E501
        """Fetch transactions by month and type for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_month_and_type1_with_http_info(account_id, month, type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str month: Month to use for the search range (required)
        :param str type: Transaction type (CREDIT, DEBIT) (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'month', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_by_month_and_type1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions_by_month_and_type1`")  # noqa: E501
        # verify the required parameter 'month' is set
        if self.api_client.client_side_validation and ('month' not in params or
                                                       params['month'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `month` when calling `get_transactions_by_month_and_type1`")  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in params or
                                                       params['type'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `type` when calling `get_transactions_by_month_and_type1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'month' in params:
            path_params['month'] = params['month']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501

        query_params = []

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
            '/accounts/{accountId}/transactions/month/{month}/type/{type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_by_to_from_date1(self, account_id, from_date, to_date, **kwargs):  # noqa: E501
        """Fetch transactions for date range for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_to_from_date1(account_id, from_date, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str from_date: Search starting date (required)
        :param str to_date: Search ending date (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_by_to_from_date1_with_http_info(account_id, from_date, to_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_by_to_from_date1_with_http_info(account_id, from_date, to_date, **kwargs)  # noqa: E501
            return data

    def get_transactions_by_to_from_date1_with_http_info(self, account_id, from_date, to_date, **kwargs):  # noqa: E501
        """Fetch transactions for date range for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_to_from_date1_with_http_info(account_id, from_date, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str from_date: Search starting date (required)
        :param str to_date: Search ending date (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'from_date', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_by_to_from_date1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions_by_to_from_date1`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if self.api_client.client_side_validation and ('from_date' not in params or
                                                       params['from_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `from_date` when calling `get_transactions_by_to_from_date1`")  # noqa: E501
        # verify the required parameter 'to_date' is set
        if self.api_client.client_side_validation and ('to_date' not in params or
                                                       params['to_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `to_date` when calling `get_transactions_by_to_from_date1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'from_date' in params:
            path_params['fromDate'] = params['from_date']  # noqa: E501
        if 'to_date' in params:
            path_params['toDate'] = params['to_date']  # noqa: E501

        query_params = []

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
            '/accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_on_date1(self, account_id, on_date, **kwargs):  # noqa: E501
        """Fetch transactions for a specific date for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_on_date1(account_id, on_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str on_date: Search specific date (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_on_date1_with_http_info(account_id, on_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_on_date1_with_http_info(account_id, on_date, **kwargs)  # noqa: E501
            return data

    def get_transactions_on_date1_with_http_info(self, account_id, on_date, **kwargs):  # noqa: E501
        """Fetch transactions for a specific date for account  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_on_date1_with_http_info(account_id, on_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: Account id (required)
        :param str on_date: Search specific date (required)
        :return: list[Transaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'on_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_on_date1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_transactions_on_date1`")  # noqa: E501
        # verify the required parameter 'on_date' is set
        if self.api_client.client_side_validation and ('on_date' not in params or
                                                       params['on_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `on_date` when calling `get_transactions_on_date1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'on_date' in params:
            path_params['onDate'] = params['on_date']  # noqa: E501

        query_params = []

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
            '/accounts/{accountId}/transactions/onDate/{onDate}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Transaction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)