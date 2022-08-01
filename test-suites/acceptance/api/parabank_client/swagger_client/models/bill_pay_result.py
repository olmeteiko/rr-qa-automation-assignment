# coding: utf-8

"""
    The ParaBank REST API

    This API provides access to various ParaBank internal operations  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: webadmin@parabank.parasoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BillPayResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payee_name': 'str',
        'amount': 'float',
        'account_id': 'int'
    }

    attribute_map = {
        'payee_name': 'payeeName',
        'amount': 'amount',
        'account_id': 'accountId'
    }

    def __init__(self, payee_name=None, amount=None, account_id=None, _configuration=None):  # noqa: E501
        """BillPayResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payee_name = None
        self._amount = None
        self._account_id = None
        self.discriminator = None

        if payee_name is not None:
            self.payee_name = payee_name
        if amount is not None:
            self.amount = amount
        if account_id is not None:
            self.account_id = account_id

    @property
    def payee_name(self):
        """Gets the payee_name of this BillPayResult.  # noqa: E501


        :return: The payee_name of this BillPayResult.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this BillPayResult.


        :param payee_name: The payee_name of this BillPayResult.  # noqa: E501
        :type: str
        """

        self._payee_name = payee_name

    @property
    def amount(self):
        """Gets the amount of this BillPayResult.  # noqa: E501


        :return: The amount of this BillPayResult.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BillPayResult.


        :param amount: The amount of this BillPayResult.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def account_id(self):
        """Gets the account_id of this BillPayResult.  # noqa: E501


        :return: The account_id of this BillPayResult.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BillPayResult.


        :param account_id: The account_id of this BillPayResult.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BillPayResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillPayResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillPayResult):
            return True

        return self.to_dict() != other.to_dict()