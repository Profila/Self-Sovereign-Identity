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

class VerificationPolicyInput(object):
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
        'name': 'str',
        'description': 'str',
        'constraints': 'list[VerificationPolicyConstraint]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'constraints': 'constraints'
    }

    def __init__(self, id=None, name=None, description=None, constraints=None):  # noqa: E501
        """VerificationPolicyInput - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._constraints = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        if constraints is not None:
            self.constraints = constraints

    @property
    def id(self):
        """Gets the id of this VerificationPolicyInput.  # noqa: E501

        A unique identifier to address the verification policy instance. UUID is generated by the backend.  # noqa: E501

        :return: The id of this VerificationPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VerificationPolicyInput.

        A unique identifier to address the verification policy instance. UUID is generated by the backend.  # noqa: E501

        :param id: The id of this VerificationPolicyInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VerificationPolicyInput.  # noqa: E501

        A human-readable name for the verification policy. The `name` cannot be empty.  # noqa: E501

        :return: The name of this VerificationPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VerificationPolicyInput.

        A human-readable name for the verification policy. The `name` cannot be empty.  # noqa: E501

        :param name: The name of this VerificationPolicyInput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VerificationPolicyInput.  # noqa: E501

        A human-readable description of the verification policy.  # noqa: E501

        :return: The description of this VerificationPolicyInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VerificationPolicyInput.

        A human-readable description of the verification policy.  # noqa: E501

        :param description: The description of this VerificationPolicyInput.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def constraints(self):
        """Gets the constraints of this VerificationPolicyInput.  # noqa: E501

        The object that describes the constraints of the verification policy. Each constraint is a tuple of the `schemaId` and a set of DIDs of the trusted issuers.  # noqa: E501

        :return: The constraints of this VerificationPolicyInput.  # noqa: E501
        :rtype: list[VerificationPolicyConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this VerificationPolicyInput.

        The object that describes the constraints of the verification policy. Each constraint is a tuple of the `schemaId` and a set of DIDs of the trusted issuers.  # noqa: E501

        :param constraints: The constraints of this VerificationPolicyInput.  # noqa: E501
        :type: list[VerificationPolicyConstraint]
        """

        self._constraints = constraints

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
        if issubclass(VerificationPolicyInput, dict):
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
        if not isinstance(other, VerificationPolicyInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
