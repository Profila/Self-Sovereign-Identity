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

class Connection(object):
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
        'connection_id': 'str',
        'thid': 'str',
        'label': 'str',
        'goal_code': 'str',
        'goal': 'str',
        'my_did': 'str',
        'their_did': 'str',
        'role': 'str',
        'state': 'str',
        'invitation': 'ConnectionInvitation',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'meta_retries': 'int',
        '_self': 'str',
        'kind': 'str'
    }

    attribute_map = {
        'connection_id': 'connectionId',
        'thid': 'thid',
        'label': 'label',
        'goal_code': 'goalCode',
        'goal': 'goal',
        'my_did': 'myDid',
        'their_did': 'theirDid',
        'role': 'role',
        'state': 'state',
        'invitation': 'invitation',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'meta_retries': 'metaRetries',
        '_self': 'self',
        'kind': 'kind'
    }

    def __init__(self, connection_id=None, thid=None, label=None, goal_code=None, goal=None, my_did=None, their_did=None, role=None, state=None, invitation=None, created_at=None, updated_at=None, meta_retries=None, _self=None, kind=None):  # noqa: E501
        """Connection - a model defined in Swagger"""  # noqa: E501
        self._connection_id = None
        self._thid = None
        self._label = None
        self._goal_code = None
        self._goal = None
        self._my_did = None
        self._their_did = None
        self._role = None
        self._state = None
        self._invitation = None
        self._created_at = None
        self._updated_at = None
        self._meta_retries = None
        self.__self = None
        self._kind = None
        self.discriminator = None
        self.connection_id = connection_id
        self.thid = thid
        if label is not None:
            self.label = label
        if goal_code is not None:
            self.goal_code = goal_code
        if goal is not None:
            self.goal = goal
        if my_did is not None:
            self.my_did = my_did
        if their_did is not None:
            self.their_did = their_did
        self.role = role
        self.state = state
        self.invitation = invitation
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.meta_retries = meta_retries
        self._self = _self
        self.kind = kind

    @property
    def connection_id(self):
        """Gets the connection_id of this Connection.  # noqa: E501

        The unique identifier of the connection.  # noqa: E501

        :return: The connection_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this Connection.

        The unique identifier of the connection.  # noqa: E501

        :param connection_id: The connection_id of this Connection.  # noqa: E501
        :type: str
        """
        if connection_id is None:
            raise ValueError("Invalid value for `connection_id`, must not be `None`")  # noqa: E501

        self._connection_id = connection_id

    @property
    def thid(self):
        """Gets the thid of this Connection.  # noqa: E501

        The unique identifier of the thread this connection record belongs to. The value will identical on both sides of the connection (inviter and invitee)  # noqa: E501

        :return: The thid of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._thid

    @thid.setter
    def thid(self, thid):
        """Sets the thid of this Connection.

        The unique identifier of the thread this connection record belongs to. The value will identical on both sides of the connection (inviter and invitee)  # noqa: E501

        :param thid: The thid of this Connection.  # noqa: E501
        :type: str
        """
        if thid is None:
            raise ValueError("Invalid value for `thid`, must not be `None`")  # noqa: E501

        self._thid = thid

    @property
    def label(self):
        """Gets the label of this Connection.  # noqa: E501

        A human readable alias for the connection.  # noqa: E501

        :return: The label of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Connection.

        A human readable alias for the connection.  # noqa: E501

        :param label: The label of this Connection.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def goal_code(self):
        """Gets the goal_code of this Connection.  # noqa: E501

        A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message.  # noqa: E501

        :return: The goal_code of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._goal_code

    @goal_code.setter
    def goal_code(self, goal_code):
        """Sets the goal_code of this Connection.

        A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message.  # noqa: E501

        :param goal_code: The goal_code of this Connection.  # noqa: E501
        :type: str
        """

        self._goal_code = goal_code

    @property
    def goal(self):
        """Gets the goal of this Connection.  # noqa: E501

        A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message.  # noqa: E501

        :return: The goal of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this Connection.

        A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message.  # noqa: E501

        :param goal: The goal of this Connection.  # noqa: E501
        :type: str
        """

        self._goal = goal

    @property
    def my_did(self):
        """Gets the my_did of this Connection.  # noqa: E501

        The DID representing me as the inviter or invitee in this specific connection.  # noqa: E501

        :return: The my_did of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._my_did

    @my_did.setter
    def my_did(self, my_did):
        """Sets the my_did of this Connection.

        The DID representing me as the inviter or invitee in this specific connection.  # noqa: E501

        :param my_did: The my_did of this Connection.  # noqa: E501
        :type: str
        """

        self._my_did = my_did

    @property
    def their_did(self):
        """Gets the their_did of this Connection.  # noqa: E501

        The DID representing the other peer as the an inviter or invitee in this specific connection.  # noqa: E501

        :return: The their_did of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._their_did

    @their_did.setter
    def their_did(self, their_did):
        """Sets the their_did of this Connection.

        The DID representing the other peer as the an inviter or invitee in this specific connection.  # noqa: E501

        :param their_did: The their_did of this Connection.  # noqa: E501
        :type: str
        """

        self._their_did = their_did

    @property
    def role(self):
        """Gets the role of this Connection.  # noqa: E501

        The role played by the Prism agent in the connection flow.  # noqa: E501

        :return: The role of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Connection.

        The role played by the Prism agent in the connection flow.  # noqa: E501

        :param role: The role of this Connection.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["Inviter", "Invitee"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def state(self):
        """Gets the state of this Connection.  # noqa: E501

        The current state of the connection protocol execution.  # noqa: E501

        :return: The state of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Connection.

        The current state of the connection protocol execution.  # noqa: E501

        :param state: The state of this Connection.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["InvitationGenerated", "InvitationReceived", "ConnectionRequestPending", "ConnectionRequestSent", "ConnectionRequestReceived", "ConnectionResponsePending", "ConnectionResponseSent", "ConnectionResponseReceived", "ProblemReportPending", "ProblemReportSent", "ProblemReportReceived"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def invitation(self):
        """Gets the invitation of this Connection.  # noqa: E501


        :return: The invitation of this Connection.  # noqa: E501
        :rtype: ConnectionInvitation
        """
        return self._invitation

    @invitation.setter
    def invitation(self, invitation):
        """Sets the invitation of this Connection.


        :param invitation: The invitation of this Connection.  # noqa: E501
        :type: ConnectionInvitation
        """
        if invitation is None:
            raise ValueError("Invalid value for `invitation`, must not be `None`")  # noqa: E501

        self._invitation = invitation

    @property
    def created_at(self):
        """Gets the created_at of this Connection.  # noqa: E501

        The date and time the connection record was created.  # noqa: E501

        :return: The created_at of this Connection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Connection.

        The date and time the connection record was created.  # noqa: E501

        :param created_at: The created_at of this Connection.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Connection.  # noqa: E501

        The date and time the connection record was last updated.  # noqa: E501

        :return: The updated_at of this Connection.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Connection.

        The date and time the connection record was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Connection.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def meta_retries(self):
        """Gets the meta_retries of this Connection.  # noqa: E501

        The maximum background processing attempts remaining for this record  # noqa: E501

        :return: The meta_retries of this Connection.  # noqa: E501
        :rtype: int
        """
        return self._meta_retries

    @meta_retries.setter
    def meta_retries(self, meta_retries):
        """Sets the meta_retries of this Connection.

        The maximum background processing attempts remaining for this record  # noqa: E501

        :param meta_retries: The meta_retries of this Connection.  # noqa: E501
        :type: int
        """
        if meta_retries is None:
            raise ValueError("Invalid value for `meta_retries`, must not be `None`")  # noqa: E501

        self._meta_retries = meta_retries

    @property
    def _self(self):
        """Gets the _self of this Connection.  # noqa: E501

        The reference to the connection resource.  # noqa: E501

        :return: The _self of this Connection.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Connection.

        The reference to the connection resource.  # noqa: E501

        :param _self: The _self of this Connection.  # noqa: E501
        :type: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def kind(self):
        """Gets the kind of this Connection.  # noqa: E501

        The type of object returned. In this case a `Connection`.  # noqa: E501

        :return: The kind of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Connection.

        The type of object returned. In this case a `Connection`.  # noqa: E501

        :param kind: The kind of this Connection.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

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
        if issubclass(Connection, dict):
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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
