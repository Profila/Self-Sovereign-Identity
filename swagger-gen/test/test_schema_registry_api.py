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
from swagger_client.api.schema_registry_api import SchemaRegistryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSchemaRegistryApi(unittest.TestCase):
    """SchemaRegistryApi unit test stubs"""

    def setUp(self):
        self.api = SchemaRegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_schema(self):
        """Test case for create_schema

        Publish new schema to the schema registry  # noqa: E501
        """
        pass

    def test_get_raw_schema_by_id(self):
        """Test case for get_raw_schema_by_id

        Fetch the schema from the registry by `guid`  # noqa: E501
        """
        pass

    def test_get_schema_by_id(self):
        """Test case for get_schema_by_id

        Fetch the schema from the registry by `guid`  # noqa: E501
        """
        pass

    def test_lookup_schemas_by_query(self):
        """Test case for lookup_schemas_by_query

        Lookup schemas by indexed fields  # noqa: E501
        """
        pass

    def test_update_schema(self):
        """Test case for update_schema

        Publish the new version of the credential schema to the schema registry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
