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

class CredentialSubject(object):
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
        'status_purpose': 'StatusPurpose',
        'encoded_list': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status_purpose': 'statusPurpose',
        'encoded_list': 'encodedList'
    }

    def __init__(self, id=None, type=None, status_purpose=None, encoded_list=None):  # noqa: E501
        """CredentialSubject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._status_purpose = None
        self._encoded_list = None
        self.discriminator = None
        self.id = id
        self.type = type
        self.status_purpose = status_purpose
        self.encoded_list = encoded_list

    @property
    def id(self):
        """Gets the id of this CredentialSubject.  # noqa: E501

        Url to resolve this particular status list credential  # noqa: E501

        :return: The id of this CredentialSubject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CredentialSubject.

        Url to resolve this particular status list credential  # noqa: E501

        :param id: The id of this CredentialSubject.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this CredentialSubject.  # noqa: E501

        Always equals to constnat value - StatusList2021  # noqa: E501

        :return: The type of this CredentialSubject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CredentialSubject.

        Always equals to constnat value - StatusList2021  # noqa: E501

        :param type: The type of this CredentialSubject.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status_purpose(self):
        """Gets the status_purpose of this CredentialSubject.  # noqa: E501


        :return: The status_purpose of this CredentialSubject.  # noqa: E501
        :rtype: StatusPurpose
        """
        return self._status_purpose

    @status_purpose.setter
    def status_purpose(self, status_purpose):
        """Sets the status_purpose of this CredentialSubject.


        :param status_purpose: The status_purpose of this CredentialSubject.  # noqa: E501
        :type: StatusPurpose
        """
        if status_purpose is None:
            raise ValueError("Invalid value for `status_purpose`, must not be `None`")  # noqa: E501

        self._status_purpose = status_purpose

    @property
    def encoded_list(self):
        """Gets the encoded_list of this CredentialSubject.  # noqa: E501

        base64 url encoded bitstring of credential statuses  # noqa: E501

        :return: The encoded_list of this CredentialSubject.  # noqa: E501
        :rtype: str
        """
        return self._encoded_list

    @encoded_list.setter
    def encoded_list(self, encoded_list):
        """Sets the encoded_list of this CredentialSubject.

        base64 url encoded bitstring of credential statuses  # noqa: E501

        :param encoded_list: The encoded_list of this CredentialSubject.  # noqa: E501
        :type: str
        """
        if encoded_list is None:
            raise ValueError("Invalid value for `encoded_list`, must not be `None`")  # noqa: E501

        self._encoded_list = encoded_list

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
        if issubclass(CredentialSubject, dict):
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
        if not isinstance(other, CredentialSubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
