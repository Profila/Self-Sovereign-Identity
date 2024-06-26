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

class Proof1(object):
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
        'type': 'str',
        'created': 'datetime',
        'verification_method': 'str',
        'proof_purpose': 'str',
        'proof_value': 'str',
        'jws': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'type': 'type',
        'created': 'created',
        'verification_method': 'verificationMethod',
        'proof_purpose': 'proofPurpose',
        'proof_value': 'proofValue',
        'jws': 'jws',
        'domain': 'domain'
    }

    def __init__(self, type=None, created=None, verification_method=None, proof_purpose=None, proof_value=None, jws=None, domain=None):  # noqa: E501
        """Proof1 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._created = None
        self._verification_method = None
        self._proof_purpose = None
        self._proof_value = None
        self._jws = None
        self._domain = None
        self.discriminator = None
        self.type = type
        self.created = created
        self.verification_method = verification_method
        self.proof_purpose = proof_purpose
        self.proof_value = proof_value
        self.jws = jws
        if domain is not None:
            self.domain = domain

    @property
    def type(self):
        """Gets the type of this Proof1.  # noqa: E501

        The type of cryptographic signature algorithm used to generate the proof.  # noqa: E501

        :return: The type of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Proof1.

        The type of cryptographic signature algorithm used to generate the proof.  # noqa: E501

        :param type: The type of this Proof1.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def created(self):
        """Gets the created of this Proof1.  # noqa: E501

        The date and time at which the proof was created, in UTC format. This field is used to ensure that the proof was generated before or at the same time as the credential schema itself.  # noqa: E501

        :return: The created of this Proof1.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Proof1.

        The date and time at which the proof was created, in UTC format. This field is used to ensure that the proof was generated before or at the same time as the credential schema itself.  # noqa: E501

        :param created: The created of this Proof1.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def verification_method(self):
        """Gets the verification_method of this Proof1.  # noqa: E501

        The verification method used to generate the proof. This is usually a DID and key ID combination that can be used to look up the public key needed to verify the proof.  # noqa: E501

        :return: The verification_method of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._verification_method

    @verification_method.setter
    def verification_method(self, verification_method):
        """Sets the verification_method of this Proof1.

        The verification method used to generate the proof. This is usually a DID and key ID combination that can be used to look up the public key needed to verify the proof.  # noqa: E501

        :param verification_method: The verification_method of this Proof1.  # noqa: E501
        :type: str
        """
        if verification_method is None:
            raise ValueError("Invalid value for `verification_method`, must not be `None`")  # noqa: E501

        self._verification_method = verification_method

    @property
    def proof_purpose(self):
        """Gets the proof_purpose of this Proof1.  # noqa: E501

        The purpose of the proof (for example: `assertionMethod`). This indicates that the proof is being used to assert that the issuer really issued this credential schema instance.  # noqa: E501

        :return: The proof_purpose of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._proof_purpose

    @proof_purpose.setter
    def proof_purpose(self, proof_purpose):
        """Sets the proof_purpose of this Proof1.

        The purpose of the proof (for example: `assertionMethod`). This indicates that the proof is being used to assert that the issuer really issued this credential schema instance.  # noqa: E501

        :param proof_purpose: The proof_purpose of this Proof1.  # noqa: E501
        :type: str
        """
        if proof_purpose is None:
            raise ValueError("Invalid value for `proof_purpose`, must not be `None`")  # noqa: E501

        self._proof_purpose = proof_purpose

    @property
    def proof_value(self):
        """Gets the proof_value of this Proof1.  # noqa: E501

        The cryptographic signature value that was generated using the private key associated with the verification method, and which can be used to verify the proof.  # noqa: E501

        :return: The proof_value of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._proof_value

    @proof_value.setter
    def proof_value(self, proof_value):
        """Sets the proof_value of this Proof1.

        The cryptographic signature value that was generated using the private key associated with the verification method, and which can be used to verify the proof.  # noqa: E501

        :param proof_value: The proof_value of this Proof1.  # noqa: E501
        :type: str
        """
        if proof_value is None:
            raise ValueError("Invalid value for `proof_value`, must not be `None`")  # noqa: E501

        self._proof_value = proof_value

    @property
    def jws(self):
        """Gets the jws of this Proof1.  # noqa: E501

        The JSON Web Signature (JWS) that contains the proof information.  # noqa: E501

        :return: The jws of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._jws

    @jws.setter
    def jws(self, jws):
        """Sets the jws of this Proof1.

        The JSON Web Signature (JWS) that contains the proof information.  # noqa: E501

        :param jws: The jws of this Proof1.  # noqa: E501
        :type: str
        """
        if jws is None:
            raise ValueError("Invalid value for `jws`, must not be `None`")  # noqa: E501

        self._jws = jws

    @property
    def domain(self):
        """Gets the domain of this Proof1.  # noqa: E501

        It specifies the domain context within which the credential schema and proof are being used  # noqa: E501

        :return: The domain of this Proof1.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Proof1.

        It specifies the domain context within which the credential schema and proof are being used  # noqa: E501

        :param domain: The domain of this Proof1.  # noqa: E501
        :type: str
        """

        self._domain = domain

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
        if issubclass(Proof1, dict):
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
        if not isinstance(other, Proof1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
