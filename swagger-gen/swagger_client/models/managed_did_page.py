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

class ManagedDIDPage(object):
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
        '_self': 'str',
        'kind': 'str',
        'page_of': 'str',
        'next': 'str',
        'previous': 'str',
        'contents': 'list[ManagedDID]'
    }

    attribute_map = {
        '_self': 'self',
        'kind': 'kind',
        'page_of': 'pageOf',
        'next': 'next',
        'previous': 'previous',
        'contents': 'contents'
    }

    def __init__(self, _self=None, kind=None, page_of=None, next=None, previous=None, contents=None):  # noqa: E501
        """ManagedDIDPage - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._kind = None
        self._page_of = None
        self._next = None
        self._previous = None
        self._contents = None
        self.discriminator = None
        self._self = _self
        self.kind = kind
        self.page_of = page_of
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous
        if contents is not None:
            self.contents = contents

    @property
    def _self(self):
        """Gets the _self of this ManagedDIDPage.  # noqa: E501


        :return: The _self of this ManagedDIDPage.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ManagedDIDPage.


        :param _self: The _self of this ManagedDIDPage.  # noqa: E501
        :type: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def kind(self):
        """Gets the kind of this ManagedDIDPage.  # noqa: E501


        :return: The kind of this ManagedDIDPage.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ManagedDIDPage.


        :param kind: The kind of this ManagedDIDPage.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def page_of(self):
        """Gets the page_of of this ManagedDIDPage.  # noqa: E501


        :return: The page_of of this ManagedDIDPage.  # noqa: E501
        :rtype: str
        """
        return self._page_of

    @page_of.setter
    def page_of(self, page_of):
        """Sets the page_of of this ManagedDIDPage.


        :param page_of: The page_of of this ManagedDIDPage.  # noqa: E501
        :type: str
        """
        if page_of is None:
            raise ValueError("Invalid value for `page_of`, must not be `None`")  # noqa: E501

        self._page_of = page_of

    @property
    def next(self):
        """Gets the next of this ManagedDIDPage.  # noqa: E501


        :return: The next of this ManagedDIDPage.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ManagedDIDPage.


        :param next: The next of this ManagedDIDPage.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this ManagedDIDPage.  # noqa: E501


        :return: The previous of this ManagedDIDPage.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this ManagedDIDPage.


        :param previous: The previous of this ManagedDIDPage.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def contents(self):
        """Gets the contents of this ManagedDIDPage.  # noqa: E501


        :return: The contents of this ManagedDIDPage.  # noqa: E501
        :rtype: list[ManagedDID]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ManagedDIDPage.


        :param contents: The contents of this ManagedDIDPage.  # noqa: E501
        :type: list[ManagedDID]
        """

        self._contents = contents

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
        if issubclass(ManagedDIDPage, dict):
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
        if not isinstance(other, ManagedDIDPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
