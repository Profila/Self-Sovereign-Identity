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

class VerificationMethod(object):
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
        'id': 'str',
        'type': 'str',
        'controller': 'str',
        'public_key_jwk': 'PublicKeyJwk'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'controller': 'controller',
        'public_key_jwk': 'publicKeyJwk'
    }

    def __init__(self, id=None, type=None, controller=None, public_key_jwk=None):  # noqa: E501
        """VerificationMethod - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._controller = None
        self._public_key_jwk = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.controller = controller
        self.public_key_jwk = public_key_jwk

    @property
    def id(self):
        """Gets the id of this VerificationMethod.  # noqa: E501

        The identifier for the verification method.  # noqa: E501

        :return: The id of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VerificationMethod.

        The identifier for the verification method.  # noqa: E501

        :param id: The id of this VerificationMethod.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this VerificationMethod.  # noqa: E501

        The type of the verification method.  # noqa: E501

        :return: The type of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VerificationMethod.

        The type of the verification method.  # noqa: E501

        :param type: The type of this VerificationMethod.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def controller(self):
        """Gets the controller of this VerificationMethod.  # noqa: E501

        The DID that controls the verification method.  # noqa: E501

        :return: The controller of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this VerificationMethod.

        The DID that controls the verification method.  # noqa: E501

        :param controller: The controller of this VerificationMethod.  # noqa: E501
        :type: str
        """
        if controller is None:
            raise ValueError("Invalid value for `controller`, must not be `None`")  # noqa: E501

        self._controller = controller

    @property
    def public_key_jwk(self):
        """Gets the public_key_jwk of this VerificationMethod.  # noqa: E501


        :return: The public_key_jwk of this VerificationMethod.  # noqa: E501
        :rtype: PublicKeyJwk
        """
        return self._public_key_jwk

    @public_key_jwk.setter
    def public_key_jwk(self, public_key_jwk):
        """Sets the public_key_jwk of this VerificationMethod.


        :param public_key_jwk: The public_key_jwk of this VerificationMethod.  # noqa: E501
        :type: PublicKeyJwk
        """
        if public_key_jwk is None:
            raise ValueError("Invalid value for `public_key_jwk`, must not be `None`")  # noqa: E501

        self._public_key_jwk = public_key_jwk

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
        if issubclass(VerificationMethod, dict):
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
        if not isinstance(other, VerificationMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
