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

class ConnectionInvitation(object):
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
        '_from': 'str',
        'invitation_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        '_from': 'from',
        'invitation_url': 'invitationUrl'
    }

    def __init__(self, id=None, type=None, _from=None, invitation_url=None):  # noqa: E501
        """ConnectionInvitation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self.__from = None
        self._invitation_url = None
        self.discriminator = None
        self.id = id
        self.type = type
        self._from = _from
        self.invitation_url = invitation_url

    @property
    def id(self):
        """Gets the id of this ConnectionInvitation.  # noqa: E501

        The unique identifier of the invitation. It should be used as parent thread ID (pthid) for the Connection Request message that follows.  # noqa: E501

        :return: The id of this ConnectionInvitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectionInvitation.

        The unique identifier of the invitation. It should be used as parent thread ID (pthid) for the Connection Request message that follows.  # noqa: E501

        :param id: The id of this ConnectionInvitation.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ConnectionInvitation.  # noqa: E501

        The DIDComm Message Type URI (MTURI) the invitation message complies with.  # noqa: E501

        :return: The type of this ConnectionInvitation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectionInvitation.

        The DIDComm Message Type URI (MTURI) the invitation message complies with.  # noqa: E501

        :param type: The type of this ConnectionInvitation.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def _from(self):
        """Gets the _from of this ConnectionInvitation.  # noqa: E501

        The DID representing the sender to be used by recipients for future interactions.  # noqa: E501

        :return: The _from of this ConnectionInvitation.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ConnectionInvitation.

        The DID representing the sender to be used by recipients for future interactions.  # noqa: E501

        :param _from: The _from of this ConnectionInvitation.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def invitation_url(self):
        """Gets the invitation_url of this ConnectionInvitation.  # noqa: E501

        The invitation message encoded as a URL. This URL follows the Out of [Band 2.0 protocol](https://identity.foundation/didcomm-messaging/spec/v2.0/#out-of-band-messages) and can be used to generate a QR code for example.  # noqa: E501

        :return: The invitation_url of this ConnectionInvitation.  # noqa: E501
        :rtype: str
        """
        return self._invitation_url

    @invitation_url.setter
    def invitation_url(self, invitation_url):
        """Sets the invitation_url of this ConnectionInvitation.

        The invitation message encoded as a URL. This URL follows the Out of [Band 2.0 protocol](https://identity.foundation/didcomm-messaging/spec/v2.0/#out-of-band-messages) and can be used to generate a QR code for example.  # noqa: E501

        :param invitation_url: The invitation_url of this ConnectionInvitation.  # noqa: E501
        :type: str
        """
        if invitation_url is None:
            raise ValueError("Invalid value for `invitation_url`, must not be `None`")  # noqa: E501

        self._invitation_url = invitation_url

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
        if issubclass(ConnectionInvitation, dict):
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
        if not isinstance(other, ConnectionInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
