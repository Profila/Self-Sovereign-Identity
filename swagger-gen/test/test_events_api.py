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
from swagger_client.api.events_api import EventsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_events_webhooks_id(self):
        """Test case for delete_events_webhooks_id

        Delete the wallet webhook notification by `id`  # noqa: E501
        """
        pass

    def test_get_events_webhooks(self):
        """Test case for get_events_webhooks

        List wallet webhook notifications  # noqa: E501
        """
        pass

    def test_post_events_webhooks(self):
        """Test case for post_events_webhooks

        Create wallet webhook notifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()