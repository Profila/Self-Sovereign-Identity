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

class StatusListCredential(object):
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
        'context': 'list[str]',
        'type': 'list[str]',
        'issuer': 'str',
        'id': 'str',
        'issuance_date': 'datetime',
        'credential_subject': 'CredentialSubject',
        'proof': 'object'
    }

    attribute_map = {
        'context': '@context',
        'type': 'type',
        'issuer': 'issuer',
        'id': 'id',
        'issuance_date': 'issuanceDate',
        'credential_subject': 'credentialSubject',
        'proof': 'proof'
    }

    def __init__(self, context=None, type=None, issuer=None, id=None, issuance_date=None, credential_subject=None, proof=None):  # noqa: E501
        """StatusListCredential - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._type = None
        self._issuer = None
        self._id = None
        self._issuance_date = None
        self._credential_subject = None
        self._proof = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if type is not None:
            self.type = type
        self.issuer = issuer
        self.id = id
        self.issuance_date = issuance_date
        self.credential_subject = credential_subject
        self.proof = proof

    @property
    def context(self):
        """Gets the context of this StatusListCredential.  # noqa: E501

        List of JSON-LD contexts  # noqa: E501

        :return: The context of this StatusListCredential.  # noqa: E501
        :rtype: list[str]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this StatusListCredential.

        List of JSON-LD contexts  # noqa: E501

        :param context: The context of this StatusListCredential.  # noqa: E501
        :type: list[str]
        """

        self._context = context

    @property
    def type(self):
        """Gets the type of this StatusListCredential.  # noqa: E501

        List of credential types  # noqa: E501

        :return: The type of this StatusListCredential.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatusListCredential.

        List of credential types  # noqa: E501

        :param type: The type of this StatusListCredential.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def issuer(self):
        """Gets the issuer of this StatusListCredential.  # noqa: E501

        DID of the issuer of status list credential  # noqa: E501

        :return: The issuer of this StatusListCredential.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this StatusListCredential.

        DID of the issuer of status list credential  # noqa: E501

        :param issuer: The issuer of this StatusListCredential.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def id(self):
        """Gets the id of this StatusListCredential.  # noqa: E501

        Unique identifier of status list credential  # noqa: E501

        :return: The id of this StatusListCredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusListCredential.

        Unique identifier of status list credential  # noqa: E501

        :param id: The id of this StatusListCredential.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def issuance_date(self):
        """Gets the issuance_date of this StatusListCredential.  # noqa: E501

        Issuance timestamp of status list credential  # noqa: E501

        :return: The issuance_date of this StatusListCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._issuance_date

    @issuance_date.setter
    def issuance_date(self, issuance_date):
        """Sets the issuance_date of this StatusListCredential.

        Issuance timestamp of status list credential  # noqa: E501

        :param issuance_date: The issuance_date of this StatusListCredential.  # noqa: E501
        :type: datetime
        """
        if issuance_date is None:
            raise ValueError("Invalid value for `issuance_date`, must not be `None`")  # noqa: E501

        self._issuance_date = issuance_date

    @property
    def credential_subject(self):
        """Gets the credential_subject of this StatusListCredential.  # noqa: E501


        :return: The credential_subject of this StatusListCredential.  # noqa: E501
        :rtype: CredentialSubject
        """
        return self._credential_subject

    @credential_subject.setter
    def credential_subject(self, credential_subject):
        """Sets the credential_subject of this StatusListCredential.


        :param credential_subject: The credential_subject of this StatusListCredential.  # noqa: E501
        :type: CredentialSubject
        """
        if credential_subject is None:
            raise ValueError("Invalid value for `credential_subject`, must not be `None`")  # noqa: E501

        self._credential_subject = credential_subject

    @property
    def proof(self):
        """Gets the proof of this StatusListCredential.  # noqa: E501

        Embedded proof to verify data integrity of status list credential, includes \"type\" property which defines an algorithm to be used for proof verification  # noqa: E501

        :return: The proof of this StatusListCredential.  # noqa: E501
        :rtype: object
        """
        return self._proof

    @proof.setter
    def proof(self, proof):
        """Sets the proof of this StatusListCredential.

        Embedded proof to verify data integrity of status list credential, includes \"type\" property which defines an algorithm to be used for proof verification  # noqa: E501

        :param proof: The proof of this StatusListCredential.  # noqa: E501
        :type: object
        """
        if proof is None:
            raise ValueError("Invalid value for `proof`, must not be `None`")  # noqa: E501

        self._proof = proof

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
        if issubclass(StatusListCredential, dict):
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
        if not isinstance(other, StatusListCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
