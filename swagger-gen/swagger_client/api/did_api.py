# coding: utf-8

"""
    Open Enterprise Agent API Reference

     The Open Enterprise Agent API facilitates the integration and management of self-sovereign identity capabilities within applications. It supports DID (Decentralized Identifiers) management, verifiable credential exchange, and secure messaging based on DIDComm standards. The API is designed to be interoperable with various blockchain and DLT (Distributed Ledger Technology) platforms, ensuring wide compatibility and flexibility. Key features include connection management, credential issuance and verification, and secure, privacy-preserving communication between entities. Additional information and the full list of capabilities can be found in the [Open Enterprise Agent documentation](https://docs.atalaprism.io/docs/category/prism-cloud-agent)   # noqa: E501

    OpenAPI spec version: 1.31.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DIDApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_did(self, did_ref, **kwargs):  # noqa: E501
        """Resolve Prism DID to a W3C representation  # noqa: E501

        Resolve Prism DID to a W3C DID document representation. The response can be the [DID resolution result](https://w3c-ccg.github.io/did-resolution/#did-resolution-result) or [DID document representation](https://www.w3.org/TR/did-core/#representations) depending on the `Accept` request header. The response is implemented according to [resolver HTTP binding](https://w3c-ccg.github.io/did-resolution/#bindings-https) in the DID resolution spec.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_did(did_ref, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did_ref: Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) (required)
        :return: DIDResolutionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_did_with_http_info(did_ref, **kwargs)  # noqa: E501
        else:
            (data) = self.get_did_with_http_info(did_ref, **kwargs)  # noqa: E501
            return data

    def get_did_with_http_info(self, did_ref, **kwargs):  # noqa: E501
        """Resolve Prism DID to a W3C representation  # noqa: E501

        Resolve Prism DID to a W3C DID document representation. The response can be the [DID resolution result](https://w3c-ccg.github.io/did-resolution/#did-resolution-result) or [DID document representation](https://www.w3.org/TR/did-core/#representations) depending on the `Accept` request header. The response is implemented according to [resolver HTTP binding](https://w3c-ccg.github.io/did-resolution/#bindings-https) in the DID resolution spec.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_did_with_http_info(did_ref, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str did_ref: Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) (required)
        :return: DIDResolutionResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did_ref']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_did" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did_ref' is set
        if ('did_ref' not in params or
                params['did_ref'] is None):
            raise ValueError("Missing the required parameter `did_ref` when calling `get_did`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did_ref' in params:
            path_params['didRef'] = params['did_ref']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json; profile=https://w3id.org/did-resolution', 'application/did+ld+json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dids/{didRef}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DIDResolutionResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)