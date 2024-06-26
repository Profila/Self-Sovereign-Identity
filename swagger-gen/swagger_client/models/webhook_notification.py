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

class WebhookNotification(object):
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
        'url': 'str',
        'custom_headers': 'MapString',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'custom_headers': 'customHeaders',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, url=None, custom_headers=None, created_at=None):  # noqa: E501
        """WebhookNotification - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._custom_headers = None
        self._created_at = None
        self.discriminator = None
        self.id = id
        self.url = url
        self.custom_headers = custom_headers
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this WebhookNotification.  # noqa: E501

        ID of webhook notification resource  # noqa: E501

        :return: The id of this WebhookNotification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookNotification.

        ID of webhook notification resource  # noqa: E501

        :param id: The id of this WebhookNotification.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def url(self):
        """Gets the url of this WebhookNotification.  # noqa: E501

        A URL of webhook for event notification  # noqa: E501

        :return: The url of this WebhookNotification.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookNotification.

        A URL of webhook for event notification  # noqa: E501

        :param url: The url of this WebhookNotification.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def custom_headers(self):
        """Gets the custom_headers of this WebhookNotification.  # noqa: E501


        :return: The custom_headers of this WebhookNotification.  # noqa: E501
        :rtype: MapString
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        """Sets the custom_headers of this WebhookNotification.


        :param custom_headers: The custom_headers of this WebhookNotification.  # noqa: E501
        :type: MapString
        """
        if custom_headers is None:
            raise ValueError("Invalid value for `custom_headers`, must not be `None`")  # noqa: E501

        self._custom_headers = custom_headers

    @property
    def created_at(self):
        """Gets the created_at of this WebhookNotification.  # noqa: E501

        A time which the webhook notification resource was created.  # noqa: E501

        :return: The created_at of this WebhookNotification.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookNotification.

        A time which the webhook notification resource was created.  # noqa: E501

        :param created_at: The created_at of this WebhookNotification.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(WebhookNotification, dict):
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
        if not isinstance(other, WebhookNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
