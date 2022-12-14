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


class Customer(object):
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
        'id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'address': 'Address',
        'phone_number': 'str',
        'ssn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address': 'address',
        'phone_number': 'phoneNumber',
        'ssn': 'ssn'
    }

    def __init__(self, id=None, first_name=None, last_name=None, address=None, phone_number=None, ssn=None, _configuration=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._first_name = None
        self._last_name = None
        self._address = None
        self._phone_number = None
        self._ssn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address is not None:
            self.address = address
        if phone_number is not None:
            self.phone_number = phone_number
        if ssn is not None:
            self.ssn = ssn

    @property
    def id(self):
        """Gets the id of this Customer.  # noqa: E501


        :return: The id of this Customer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customer.


        :param id: The id of this Customer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this Customer.  # noqa: E501


        :return: The first_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.  # noqa: E501


        :return: The last_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def address(self):
        """Gets the address of this Customer.  # noqa: E501


        :return: The address of this Customer.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Customer.


        :param address: The address of this Customer.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def phone_number(self):
        """Gets the phone_number of this Customer.  # noqa: E501


        :return: The phone_number of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Customer.


        :param phone_number: The phone_number of this Customer.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def ssn(self):
        """Gets the ssn of this Customer.  # noqa: E501


        :return: The ssn of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """Sets the ssn of this Customer.


        :param ssn: The ssn of this Customer.  # noqa: E501
        :type: str
        """

        self._ssn = ssn

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
        if issubclass(Customer, dict):
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
        if not isinstance(other, Customer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Customer):
            return True

        return self.to_dict() != other.to_dict()
