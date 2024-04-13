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

class AnoncredRequestedAttributeV1(object):
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
        'name': 'str',
        'restrictions': 'list[MapString]',
        'non_revoked': 'AnoncredNonRevokedIntervalV1'
    }

    attribute_map = {
        'name': 'name',
        'restrictions': 'restrictions',
        'non_revoked': 'non_revoked'
    }

    def __init__(self, name=None, restrictions=None, non_revoked=None):  # noqa: E501
        """AnoncredRequestedAttributeV1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._restrictions = None
        self._non_revoked = None
        self.discriminator = None
        self.name = name
        if restrictions is not None:
            self.restrictions = restrictions
        if non_revoked is not None:
            self.non_revoked = non_revoked

    @property
    def name(self):
        """Gets the name of this AnoncredRequestedAttributeV1.  # noqa: E501


        :return: The name of this AnoncredRequestedAttributeV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnoncredRequestedAttributeV1.


        :param name: The name of this AnoncredRequestedAttributeV1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def restrictions(self):
        """Gets the restrictions of this AnoncredRequestedAttributeV1.  # noqa: E501


        :return: The restrictions of this AnoncredRequestedAttributeV1.  # noqa: E501
        :rtype: list[MapString]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this AnoncredRequestedAttributeV1.


        :param restrictions: The restrictions of this AnoncredRequestedAttributeV1.  # noqa: E501
        :type: list[MapString]
        """

        self._restrictions = restrictions

    @property
    def non_revoked(self):
        """Gets the non_revoked of this AnoncredRequestedAttributeV1.  # noqa: E501


        :return: The non_revoked of this AnoncredRequestedAttributeV1.  # noqa: E501
        :rtype: AnoncredNonRevokedIntervalV1
        """
        return self._non_revoked

    @non_revoked.setter
    def non_revoked(self, non_revoked):
        """Sets the non_revoked of this AnoncredRequestedAttributeV1.


        :param non_revoked: The non_revoked of this AnoncredRequestedAttributeV1.  # noqa: E501
        :type: AnoncredNonRevokedIntervalV1
        """

        self._non_revoked = non_revoked

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
        if issubclass(AnoncredRequestedAttributeV1, dict):
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
        if not isinstance(other, AnoncredRequestedAttributeV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
