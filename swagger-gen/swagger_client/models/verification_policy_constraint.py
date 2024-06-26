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

class VerificationPolicyConstraint(object):
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
        'schema_id': 'str',
        'trusted_issuers': 'list[str]'
    }

    attribute_map = {
        'schema_id': 'schemaId',
        'trusted_issuers': 'trustedIssuers'
    }

    def __init__(self, schema_id=None, trusted_issuers=None):  # noqa: E501
        """VerificationPolicyConstraint - a model defined in Swagger"""  # noqa: E501
        self._schema_id = None
        self._trusted_issuers = None
        self.discriminator = None
        self.schema_id = schema_id
        if trusted_issuers is not None:
            self.trusted_issuers = trusted_issuers

    @property
    def schema_id(self):
        """Gets the schema_id of this VerificationPolicyConstraint.  # noqa: E501

        The schema ID of the credential that is being verified.  # noqa: E501

        :return: The schema_id of this VerificationPolicyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this VerificationPolicyConstraint.

        The schema ID of the credential that is being verified.  # noqa: E501

        :param schema_id: The schema_id of this VerificationPolicyConstraint.  # noqa: E501
        :type: str
        """
        if schema_id is None:
            raise ValueError("Invalid value for `schema_id`, must not be `None`")  # noqa: E501

        self._schema_id = schema_id

    @property
    def trusted_issuers(self):
        """Gets the trusted_issuers of this VerificationPolicyConstraint.  # noqa: E501

        A list of DIDs of the trusted issuers.  # noqa: E501

        :return: The trusted_issuers of this VerificationPolicyConstraint.  # noqa: E501
        :rtype: list[str]
        """
        return self._trusted_issuers

    @trusted_issuers.setter
    def trusted_issuers(self, trusted_issuers):
        """Sets the trusted_issuers of this VerificationPolicyConstraint.

        A list of DIDs of the trusted issuers.  # noqa: E501

        :param trusted_issuers: The trusted_issuers of this VerificationPolicyConstraint.  # noqa: E501
        :type: list[str]
        """

        self._trusted_issuers = trusted_issuers

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
        if issubclass(VerificationPolicyConstraint, dict):
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
        if not isinstance(other, VerificationPolicyConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
