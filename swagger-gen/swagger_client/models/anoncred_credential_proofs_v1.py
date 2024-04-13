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

class AnoncredCredentialProofsV1(object):
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
        'credential_proofs': 'list[AnoncredCredentialProofV1]'
    }

    attribute_map = {
        'credential_proofs': 'credentialProofs'
    }

    def __init__(self, credential_proofs=None):  # noqa: E501
        """AnoncredCredentialProofsV1 - a model defined in Swagger"""  # noqa: E501
        self._credential_proofs = None
        self.discriminator = None
        if credential_proofs is not None:
            self.credential_proofs = credential_proofs

    @property
    def credential_proofs(self):
        """Gets the credential_proofs of this AnoncredCredentialProofsV1.  # noqa: E501


        :return: The credential_proofs of this AnoncredCredentialProofsV1.  # noqa: E501
        :rtype: list[AnoncredCredentialProofV1]
        """
        return self._credential_proofs

    @credential_proofs.setter
    def credential_proofs(self, credential_proofs):
        """Sets the credential_proofs of this AnoncredCredentialProofsV1.


        :param credential_proofs: The credential_proofs of this AnoncredCredentialProofsV1.  # noqa: E501
        :type: list[AnoncredCredentialProofV1]
        """

        self._credential_proofs = credential_proofs

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
        if issubclass(AnoncredCredentialProofsV1, dict):
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
        if not isinstance(other, AnoncredCredentialProofsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
