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

class UpdateManagedDIDServiceAction(object):
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
        'type': 'OneOfUpdateManagedDIDServiceActionType',
        'service_endpoint': 'Json'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'service_endpoint': 'serviceEndpoint'
    }

    def __init__(self, id=None, type=None, service_endpoint=None):  # noqa: E501
        """UpdateManagedDIDServiceAction - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._service_endpoint = None
        self.discriminator = None
        self.id = id
        if type is not None:
            self.type = type
        if service_endpoint is not None:
            self.service_endpoint = service_endpoint

    @property
    def id(self):
        """Gets the id of this UpdateManagedDIDServiceAction.  # noqa: E501

        The id of the service to update  # noqa: E501

        :return: The id of this UpdateManagedDIDServiceAction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateManagedDIDServiceAction.

        The id of the service to update  # noqa: E501

        :param id: The id of this UpdateManagedDIDServiceAction.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this UpdateManagedDIDServiceAction.  # noqa: E501

        The type of the service  # noqa: E501

        :return: The type of this UpdateManagedDIDServiceAction.  # noqa: E501
        :rtype: OneOfUpdateManagedDIDServiceActionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateManagedDIDServiceAction.

        The type of the service  # noqa: E501

        :param type: The type of this UpdateManagedDIDServiceAction.  # noqa: E501
        :type: OneOfUpdateManagedDIDServiceActionType
        """

        self._type = type

    @property
    def service_endpoint(self):
        """Gets the service_endpoint of this UpdateManagedDIDServiceAction.  # noqa: E501


        :return: The service_endpoint of this UpdateManagedDIDServiceAction.  # noqa: E501
        :rtype: Json
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        """Sets the service_endpoint of this UpdateManagedDIDServiceAction.


        :param service_endpoint: The service_endpoint of this UpdateManagedDIDServiceAction.  # noqa: E501
        :type: Json
        """

        self._service_endpoint = service_endpoint

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
        if issubclass(UpdateManagedDIDServiceAction, dict):
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
        if not isinstance(other, UpdateManagedDIDServiceAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
