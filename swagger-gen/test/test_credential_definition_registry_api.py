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
from swagger_client.api.credential_definition_registry_api import CredentialDefinitionRegistryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCredentialDefinitionRegistryApi(unittest.TestCase):
    """CredentialDefinitionRegistryApi unit test stubs"""

    def setUp(self):
        self.api = CredentialDefinitionRegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_credential_definition(self):
        """Test case for create_credential_definition

        Publish new definition to the definition registry  # noqa: E501
        """
        pass

    def test_get_credential_definition_by_id(self):
        """Test case for get_credential_definition_by_id

        Fetch the credential definition from the registry by `guid`  # noqa: E501
        """
        pass

    def test_get_credential_definition_inner_definition_by_id(self):
        """Test case for get_credential_definition_inner_definition_by_id

        Fetch the inner definition field of the credential definition from the registry by `guid`  # noqa: E501
        """
        pass

    def test_lookup_credential_definitions_by_query(self):
        """Test case for lookup_credential_definitions_by_query

        Lookup credential definitions by indexed fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()