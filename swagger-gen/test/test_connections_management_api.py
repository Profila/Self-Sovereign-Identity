# coding: utf-8

"""
    Open Enterprise Agent API Reference

     The Open Enterprise Agent API facilitates the integration and management of self-sovereign identity capabilities within applications. It supports DID (Decentralized Identifiers) management, verifiable credential exchange, and secure messaging based on DIDComm standards. The API is designed to be interoperable with various blockchain and DLT (Distributed Ledger Technology) platforms, ensuring wide compatibility and flexibility. Key features include connection management, credential issuance and verification, and secure, privacy-preserving communication between entities. Additional information and the full list of capabilities can be found in the [Open Enterprise Agent documentation](https://docs.atalaprism.io/docs/category/prism-cloud-agent)   # noqa: E501

    OpenAPI spec version: 1.31.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.connections_management_api import ConnectionsManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConnectionsManagementApi(unittest.TestCase):
    """ConnectionsManagementApi unit test stubs"""

    def setUp(self):
        self.api = ConnectionsManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_connection_invitation(self):
        """Test case for accept_connection_invitation

        Accept a new connection invitation received out-of-band from another peer Agent.  # noqa: E501
        """
        pass

    def test_create_connection(self):
        """Test case for create_connection

        Create a new connection invitation that can be delivered out-of-band to a peer Agent.  # noqa: E501
        """
        pass

    def test_get_connection(self):
        """Test case for get_connection

        Retrieves a specific connection flow record from the Agent's database based on its unique `connectionId`.  # noqa: E501
        """
        pass

    def test_get_connections(self):
        """Test case for get_connections

        Retrieves the list of connection flow records available from the Agent's database.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
