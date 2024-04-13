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


class WalletManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_wallet(self, body, **kwargs):  # noqa: E501
        """Create a new wallet  # noqa: E501

        Create a new wallet with the option to provide the seed. The seed will be used for all PRISM DID keypair derivation within the wallet.  If the role is admin, a wallet can be created at any time. If the role is tenant, a wallet can only be created if there is no existing wallet permission for that tenant. The permission for the tenant will be automatically granted after the wallet is created with tenant role.           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWalletRequest body: (required)
        :return: WalletDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_wallet_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_wallet_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_wallet_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new wallet  # noqa: E501

        Create a new wallet with the option to provide the seed. The seed will be used for all PRISM DID keypair derivation within the wallet.  If the role is admin, a wallet can be created at any time. If the role is tenant, a wallet can only be created if there is no existing wallet permission for that tenant. The permission for the tenant will be automatically granted after the wallet is created with tenant role.           # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWalletRequest body: (required)
        :return: WalletDetail
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
                    " to method create_wallet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_wallet`")  # noqa: E501

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
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WalletDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_wallet_uma_permission(self, body, wallet_id, **kwargs):  # noqa: E501
        """Create a UMA resource permission on an authorization server for the wallet.  # noqa: E501

        Create a UMA resource permission on an authorization server for the wallet. This grants the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.             # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_uma_permission(body, wallet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWalletUmaPermissionRequest body: (required)
        :param str wallet_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_wallet_uma_permission_with_http_info(body, wallet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_wallet_uma_permission_with_http_info(body, wallet_id, **kwargs)  # noqa: E501
            return data

    def create_wallet_uma_permission_with_http_info(self, body, wallet_id, **kwargs):  # noqa: E501
        """Create a UMA resource permission on an authorization server for the wallet.  # noqa: E501

        Create a UMA resource permission on an authorization server for the wallet. This grants the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.             # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wallet_uma_permission_with_http_info(body, wallet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateWalletUmaPermissionRequest body: (required)
        :param str wallet_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'wallet_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_wallet_uma_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_wallet_uma_permission`")  # noqa: E501
        # verify the required parameter 'wallet_id' is set
        if ('wallet_id' not in params or
                params['wallet_id'] is None):
            raise ValueError("Missing the required parameter `wallet_id` when calling `create_wallet_uma_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wallet_id' in params:
            path_params['walletId'] = params['wallet_id']  # noqa: E501

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
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallets/{walletId}/uma-permissions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_wallet_uma_permission(self, wallet_id, subject, **kwargs):  # noqa: E501
        """Delete a UMA resource permission on an authorization server for the wallet.  # noqa: E501

        Remove a UMA resource permission on an authorization server for the wallet. This remove the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.             # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wallet_uma_permission(wallet_id, subject, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wallet_id: (required)
        :param str subject: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_wallet_uma_permission_with_http_info(wallet_id, subject, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_wallet_uma_permission_with_http_info(wallet_id, subject, **kwargs)  # noqa: E501
            return data

    def delete_wallet_uma_permission_with_http_info(self, wallet_id, subject, **kwargs):  # noqa: E501
        """Delete a UMA resource permission on an authorization server for the wallet.  # noqa: E501

        Remove a UMA resource permission on an authorization server for the wallet. This remove the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.             # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_wallet_uma_permission_with_http_info(wallet_id, subject, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wallet_id: (required)
        :param str subject: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wallet_id', 'subject']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_wallet_uma_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wallet_id' is set
        if ('wallet_id' not in params or
                params['wallet_id'] is None):
            raise ValueError("Missing the required parameter `wallet_id` when calling `delete_wallet_uma_permission`")  # noqa: E501
        # verify the required parameter 'subject' is set
        if ('subject' not in params or
                params['subject'] is None):
            raise ValueError("Missing the required parameter `subject` when calling `delete_wallet_uma_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wallet_id' in params:
            path_params['walletId'] = params['wallet_id']  # noqa: E501

        query_params = []
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallets/{walletId}/uma-permissions', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wallets(self, **kwargs):  # noqa: E501
        """List all permitted wallets  # noqa: E501

        List all permitted wallets. If the role is admin, returns all the wallets. If the role is tenant, only return permitted wallets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :return: WalletDetailPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wallets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_wallets_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_wallets_with_http_info(self, **kwargs):  # noqa: E501
        """List all permitted wallets  # noqa: E501

        List all permitted wallets. If the role is admin, returns all the wallets. If the role is tenant, only return permitted wallets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :return: WalletDetailPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wallets" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WalletDetailPage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_wallets_walletid(self, wallet_id, **kwargs):  # noqa: E501
        """Get the wallet by ID  # noqa: E501

        Get the wallet by ID. If the role is tenant, only search the ID of permitted wallets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallets_walletid(wallet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wallet_id: (required)
        :return: WalletDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_wallets_walletid_with_http_info(wallet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_wallets_walletid_with_http_info(wallet_id, **kwargs)  # noqa: E501
            return data

    def get_wallets_walletid_with_http_info(self, wallet_id, **kwargs):  # noqa: E501
        """Get the wallet by ID  # noqa: E501

        Get the wallet by ID. If the role is tenant, only search the ID of permitted wallets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_wallets_walletid_with_http_info(wallet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str wallet_id: (required)
        :return: WalletDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wallet_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wallets_walletid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wallet_id' is set
        if ('wallet_id' not in params or
                params['wallet_id'] is None):
            raise ValueError("Missing the required parameter `wallet_id` when calling `get_wallets_walletid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wallet_id' in params:
            path_params['walletId'] = params['wallet_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['adminApiKeyAuth', 'apiKeyAuth', 'jwtAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallets/{walletId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WalletDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)