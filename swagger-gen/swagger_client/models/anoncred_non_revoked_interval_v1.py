# coding: utf-8

"""
    Open Enterprise Agent API Reference

     The Open Enterprise Agent API facilitates the integration and management of self-sovereign identity capabilities within applications. It supports DID (Decentralized Identifiers) management, verifiable credential exchange, and secure messaging based on DIDComm standards. The API is designed to be interoperable with various blockchain and DLT (Distributed Ledger Technology) platforms, ensuring wide compatibility and flexibility. Key features include connection management, credential issuance and verification, and secure, privacy-preserving communication between entities. Additional information and the full list of capabilities can be found in the [Open Enterprise Agent documentation](https://docs.atalaprism.io/docs/category/prism-cloud-agent)   # noqa: E501

    OpenAPI spec version: 1.31.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnoncredNonRevokedIntervalV1(object):
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
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, _from=None, to=None):  # noqa: E501
        """AnoncredNonRevokedIntervalV1 - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def _from(self):
        """Gets the _from of this AnoncredNonRevokedIntervalV1.  # noqa: E501


        :return: The _from of this AnoncredNonRevokedIntervalV1.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this AnoncredNonRevokedIntervalV1.


        :param _from: The _from of this AnoncredNonRevokedIntervalV1.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this AnoncredNonRevokedIntervalV1.  # noqa: E501


        :return: The to of this AnoncredNonRevokedIntervalV1.  # noqa: E501
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this AnoncredNonRevokedIntervalV1.


        :param to: The to of this AnoncredNonRevokedIntervalV1.  # noqa: E501
        :type: int
        """

        self._to = to

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
        if issubclass(AnoncredNonRevokedIntervalV1, dict):
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
        if not isinstance(other, AnoncredNonRevokedIntervalV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
