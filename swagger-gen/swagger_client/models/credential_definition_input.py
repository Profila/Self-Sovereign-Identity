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

class CredentialDefinitionInput(object):
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
        'name': 'str',
        'description': 'str',
        'version': 'str',
        'tag': 'str',
        'author': 'str',
        'schema_id': 'str',
        'signature_type': 'str',
        'support_revocation': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'version': 'version',
        'tag': 'tag',
        'author': 'author',
        'schema_id': 'schemaId',
        'signature_type': 'signatureType',
        'support_revocation': 'supportRevocation'
    }

    def __init__(self, name=None, description=None, version=None, tag=None, author=None, schema_id=None, signature_type=None, support_revocation=None):  # noqa: E501
        """CredentialDefinitionInput - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._version = None
        self._tag = None
        self._author = None
        self._schema_id = None
        self._signature_type = None
        self._support_revocation = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.version = version
        self.tag = tag
        self.author = author
        self.schema_id = schema_id
        self.signature_type = signature_type
        self.support_revocation = support_revocation

    @property
    def name(self):
        """Gets the name of this CredentialDefinitionInput.  # noqa: E501

        A human-readable name for the credential definition. A piece of Metadata.  # noqa: E501

        :return: The name of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CredentialDefinitionInput.

        A human-readable name for the credential definition. A piece of Metadata.  # noqa: E501

        :param name: The name of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CredentialDefinitionInput.  # noqa: E501

        A human-readable description of the credential definition  # noqa: E501

        :return: The description of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CredentialDefinitionInput.

        A human-readable description of the credential definition  # noqa: E501

        :param description: The description of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this CredentialDefinitionInput.  # noqa: E501

        Denotes the revision of a given Credential Definition. It should follow semantic version convention to describe the impact of the credential definition evolution.  # noqa: E501

        :return: The version of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CredentialDefinitionInput.

        Denotes the revision of a given Credential Definition. It should follow semantic version convention to describe the impact of the credential definition evolution.  # noqa: E501

        :param version: The version of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def tag(self):
        """Gets the tag of this CredentialDefinitionInput.  # noqa: E501

        Token that allow to lookup and filter the credential definition records.  # noqa: E501

        :return: The tag of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CredentialDefinitionInput.

        Token that allow to lookup and filter the credential definition records.  # noqa: E501

        :param tag: The tag of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def author(self):
        """Gets the author of this CredentialDefinitionInput.  # noqa: E501

        DID of the identity which authored the credential definition. A piece of Metadata.  # noqa: E501

        :return: The author of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CredentialDefinitionInput.

        DID of the identity which authored the credential definition. A piece of Metadata.  # noqa: E501

        :param author: The author of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def schema_id(self):
        """Gets the schema_id of this CredentialDefinitionInput.  # noqa: E501

        The unique identifier of the schema used for this credential definition.  # noqa: E501

        :return: The schema_id of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this CredentialDefinitionInput.

        The unique identifier of the schema used for this credential definition.  # noqa: E501

        :param schema_id: The schema_id of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if schema_id is None:
            raise ValueError("Invalid value for `schema_id`, must not be `None`")  # noqa: E501

        self._schema_id = schema_id

    @property
    def signature_type(self):
        """Gets the signature_type of this CredentialDefinitionInput.  # noqa: E501

        Signature type used in the CredentialDefinition.  # noqa: E501

        :return: The signature_type of this CredentialDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this CredentialDefinitionInput.

        Signature type used in the CredentialDefinition.  # noqa: E501

        :param signature_type: The signature_type of this CredentialDefinitionInput.  # noqa: E501
        :type: str
        """
        if signature_type is None:
            raise ValueError("Invalid value for `signature_type`, must not be `None`")  # noqa: E501

        self._signature_type = signature_type

    @property
    def support_revocation(self):
        """Gets the support_revocation of this CredentialDefinitionInput.  # noqa: E501

        Boolean flag indicating whether revocation is supported for this CredentialDefinition.  # noqa: E501

        :return: The support_revocation of this CredentialDefinitionInput.  # noqa: E501
        :rtype: bool
        """
        return self._support_revocation

    @support_revocation.setter
    def support_revocation(self, support_revocation):
        """Sets the support_revocation of this CredentialDefinitionInput.

        Boolean flag indicating whether revocation is supported for this CredentialDefinition.  # noqa: E501

        :param support_revocation: The support_revocation of this CredentialDefinitionInput.  # noqa: E501
        :type: bool
        """
        if support_revocation is None:
            raise ValueError("Invalid value for `support_revocation`, must not be `None`")  # noqa: E501

        self._support_revocation = support_revocation

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
        if issubclass(CredentialDefinitionInput, dict):
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
        if not isinstance(other, CredentialDefinitionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
