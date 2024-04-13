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


class SchemaRegistryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_schema(self, body, **kwargs):  # noqa: E501
        """Publish new schema to the schema registry  # noqa: E501

        Create the new credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schema(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CredentialSchemaInput body: JSON object required for the credential schema creation (required)
        :return: CredentialSchemaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_schema_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_schema_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_schema_with_http_info(self, body, **kwargs):  # noqa: E501
        """Publish new schema to the schema registry  # noqa: E501

        Create the new credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schema_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CredentialSchemaInput body: JSON object required for the credential schema creation (required)
        :return: CredentialSchemaResponse
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
                    " to method create_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_schema`")  # noqa: E501

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
            '/schema-registry/schemas', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredentialSchemaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_raw_schema_by_id(self, guid, **kwargs):  # noqa: E501
        """Fetch the schema from the registry by `guid`  # noqa: E501

        Fetch the credential schema by the unique identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_raw_schema_by_id(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_raw_schema_by_id_with_http_info(guid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_raw_schema_by_id_with_http_info(guid, **kwargs)  # noqa: E501
            return data

    def get_raw_schema_by_id_with_http_info(self, guid, **kwargs):  # noqa: E501
        """Fetch the schema from the registry by `guid`  # noqa: E501

        Fetch the credential schema by the unique identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_raw_schema_by_id_with_http_info(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_raw_schema_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `get_raw_schema_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

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
            '/schema-registry/schemas/{guid}/schema', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_schema_by_id(self, guid, **kwargs):  # noqa: E501
        """Fetch the schema from the registry by `guid`  # noqa: E501

        Fetch the credential schema by the unique identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schema_by_id(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: Globally unique identifier of the credential schema record (required)
        :return: CredentialSchemaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schema_by_id_with_http_info(guid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schema_by_id_with_http_info(guid, **kwargs)  # noqa: E501
            return data

    def get_schema_by_id_with_http_info(self, guid, **kwargs):  # noqa: E501
        """Fetch the schema from the registry by `guid`  # noqa: E501

        Fetch the credential schema by the unique identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schema_by_id_with_http_info(guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str guid: Globally unique identifier of the credential schema record (required)
        :return: CredentialSchemaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schema_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'guid' is set
        if ('guid' not in params or
                params['guid'] is None):
            raise ValueError("Missing the required parameter `guid` when calling `get_schema_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

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
            '/schema-registry/schemas/{guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredentialSchemaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lookup_schemas_by_query(self, **kwargs):  # noqa: E501
        """Lookup schemas by indexed fields  # noqa: E501

        Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and `limit` parameters   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_schemas_by_query(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str author:
        :param str name:
        :param str version:
        :param str tags:
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :param str order:
        :return: CredentialSchemaResponsePage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lookup_schemas_by_query_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.lookup_schemas_by_query_with_http_info(**kwargs)  # noqa: E501
            return data

    def lookup_schemas_by_query_with_http_info(self, **kwargs):  # noqa: E501
        """Lookup schemas by indexed fields  # noqa: E501

        Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and `limit` parameters   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_schemas_by_query_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str author:
        :param str name:
        :param str version:
        :param str tags:
        :param int offset: The number of items to skip before returning results. Default is 0 if not specified.
        :param int limit: The maximum number of items to return. Defaults to 100 if not specified.
        :param str order:
        :return: CredentialSchemaResponsePage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['author', 'name', 'version', 'tags', 'offset', 'limit', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_schemas_by_query" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'author' in params:
            query_params.append(('author', params['author']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'tags' in params:
            query_params.append(('tags', params['tags']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

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
            '/schema-registry/schemas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredentialSchemaResponsePage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schema(self, body, author, id, **kwargs):  # noqa: E501
        """Publish the new version of the credential schema to the schema registry  # noqa: E501

        Publish the new version of the credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schema(body, author, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CredentialSchemaInput body: JSON object required for the credential schema update (required)
        :param str author: DID of the identity which authored the credential schema. A piece of Metadata. (required)
        :param str id: A locally unique identifier to address the schema. UUID is generated by the backend. (required)
        :return: CredentialSchemaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schema_with_http_info(body, author, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schema_with_http_info(body, author, id, **kwargs)  # noqa: E501
            return data

    def update_schema_with_http_info(self, body, author, id, **kwargs):  # noqa: E501
        """Publish the new version of the credential schema to the schema registry  # noqa: E501

        Publish the new version of the credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schema_with_http_info(body, author, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CredentialSchemaInput body: JSON object required for the credential schema update (required)
        :param str author: DID of the identity which authored the credential schema. A piece of Metadata. (required)
        :param str id: A locally unique identifier to address the schema. UUID is generated by the backend. (required)
        :return: CredentialSchemaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'author', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_schema`")  # noqa: E501
        # verify the required parameter 'author' is set
        if ('author' not in params or
                params['author'] is None):
            raise ValueError("Missing the required parameter `author` when calling `update_schema`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_schema`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'author' in params:
            path_params['author'] = params['author']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/schema-registry/{author}/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CredentialSchemaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)