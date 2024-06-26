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


class PresentProofApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_presentation(self, **kwargs):  # noqa: E501
        """Gets the list of proof presentation records.  # noqa: E501

        list of presentation statuses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_presentation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :param str thid:
        :return: PresentationStatusPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_presentation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_presentation_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_presentation_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the list of proof presentation records.  # noqa: E501

        list of presentation statuses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_presentation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :param str thid:
        :return: PresentationStatusPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'thid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_presentation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'thid' in params:
            query_params.append(('thid', params['thid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/present-proof/presentations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PresentationStatusPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_presentation(self, presentation_id, **kwargs):  # noqa: E501
        """Gets an existing proof presentation record by its unique identifier. More information on the error can be found in the response body.  # noqa: E501

        Returns an existing presentation record by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_presentation(presentation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str presentation_id: The unique identifier of the presentation record. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_presentation_with_http_info(presentation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_presentation_with_http_info(presentation_id, **kwargs)  # noqa: E501
            return data

    def get_presentation_with_http_info(self, presentation_id, **kwargs):  # noqa: E501
        """Gets an existing proof presentation record by its unique identifier. More information on the error can be found in the response body.  # noqa: E501

        Returns an existing presentation record by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_presentation_with_http_info(presentation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str presentation_id: The unique identifier of the presentation record. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['presentation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_presentation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'presentation_id' is set
        if ('presentation_id' not in params or
                params['presentation_id'] is None):
            raise ValueError("Missing the required parameter `presentation_id` when calling `get_presentation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'presentation_id' in params:
            path_params['presentationId'] = params['presentation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/present-proof/presentations/{presentationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PresentationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_presentation(self, body, **kwargs):  # noqa: E501
        """As a Verifier, create a new proof presentation request and send it to the Prover.  # noqa: E501

        Holder presents proof derived from the verifiable credential to verifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_presentation(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestPresentationInput body: The present proof creation request. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_presentation_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.request_presentation_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def request_presentation_with_http_info(self, body, **kwargs):  # noqa: E501
        """As a Verifier, create a new proof presentation request and send it to the Prover.  # noqa: E501

        Holder presents proof derived from the verifiable credential to verifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_presentation_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestPresentationInput body: The present proof creation request. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_presentation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `request_presentation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/present-proof/presentations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PresentationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_presentation(self, body, presentation_id, **kwargs):  # noqa: E501
        """Updates the proof presentation record matching the unique identifier, with the specific action to perform.  # noqa: E501

        Accept or reject presentation of proof request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_presentation(body, presentation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestPresentationAction body: The action to perform on the proof presentation record. (required)
        :param str presentation_id: The unique identifier of the presentation record. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_presentation_with_http_info(body, presentation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_presentation_with_http_info(body, presentation_id, **kwargs)  # noqa: E501
            return data

    def update_presentation_with_http_info(self, body, presentation_id, **kwargs):  # noqa: E501
        """Updates the proof presentation record matching the unique identifier, with the specific action to perform.  # noqa: E501

        Accept or reject presentation of proof request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_presentation_with_http_info(body, presentation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestPresentationAction body: The action to perform on the proof presentation record. (required)
        :param str presentation_id: The unique identifier of the presentation record. (required)
        :return: PresentationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'presentation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_presentation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_presentation`")  # noqa: E501
        # verify the required parameter 'presentation_id' is set
        if ('presentation_id' not in params or
                params['presentation_id'] is None):
            raise ValueError("Missing the required parameter `presentation_id` when calling `update_presentation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'presentation_id' in params:
            path_params['presentationId'] = params['presentation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/present-proof/presentations/{presentationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PresentationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
