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

class RequestPresentationAction(object):
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
        'action': 'str',
        'proof_id': 'list[str]',
        'anoncred_presentation_request': 'AnoncredCredentialProofsV1'
    }

    attribute_map = {
        'action': 'action',
        'proof_id': 'proofId',
        'anoncred_presentation_request': 'anoncredPresentationRequest'
    }

    def __init__(self, action=None, proof_id=None, anoncred_presentation_request=None):  # noqa: E501
        """RequestPresentationAction - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._proof_id = None
        self._anoncred_presentation_request = None
        self.discriminator = None
        self.action = action
        if proof_id is not None:
            self.proof_id = proof_id
        if anoncred_presentation_request is not None:
            self.anoncred_presentation_request = anoncred_presentation_request

    @property
    def action(self):
        """Gets the action of this RequestPresentationAction.  # noqa: E501

        The action to perform on the proof presentation record.  # noqa: E501

        :return: The action of this RequestPresentationAction.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RequestPresentationAction.

        The action to perform on the proof presentation record.  # noqa: E501

        :param action: The action of this RequestPresentationAction.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["request-accept", "request-reject", "presentation-accept", "presentation-reject"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def proof_id(self):
        """Gets the proof_id of this RequestPresentationAction.  # noqa: E501

        The unique identifier of the issue credential record - and hence VC - to use as the prover accepts the presentation request. Only applicable on the prover side when the action is `request-accept`.  # noqa: E501

        :return: The proof_id of this RequestPresentationAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._proof_id

    @proof_id.setter
    def proof_id(self, proof_id):
        """Sets the proof_id of this RequestPresentationAction.

        The unique identifier of the issue credential record - and hence VC - to use as the prover accepts the presentation request. Only applicable on the prover side when the action is `request-accept`.  # noqa: E501

        :param proof_id: The proof_id of this RequestPresentationAction.  # noqa: E501
        :type: list[str]
        """

        self._proof_id = proof_id

    @property
    def anoncred_presentation_request(self):
        """Gets the anoncred_presentation_request of this RequestPresentationAction.  # noqa: E501


        :return: The anoncred_presentation_request of this RequestPresentationAction.  # noqa: E501
        :rtype: AnoncredCredentialProofsV1
        """
        return self._anoncred_presentation_request

    @anoncred_presentation_request.setter
    def anoncred_presentation_request(self, anoncred_presentation_request):
        """Sets the anoncred_presentation_request of this RequestPresentationAction.


        :param anoncred_presentation_request: The anoncred_presentation_request of this RequestPresentationAction.  # noqa: E501
        :type: AnoncredCredentialProofsV1
        """

        self._anoncred_presentation_request = anoncred_presentation_request

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
        if issubclass(RequestPresentationAction, dict):
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
        if not isinstance(other, RequestPresentationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
