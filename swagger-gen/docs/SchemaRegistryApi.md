# swagger_client.SchemaRegistryApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schema**](SchemaRegistryApi.md#create_schema) | **POST** /schema-registry/schemas | Publish new schema to the schema registry
[**get_raw_schema_by_id**](SchemaRegistryApi.md#get_raw_schema_by_id) | **GET** /schema-registry/schemas/{guid}/schema | Fetch the schema from the registry by &#x60;guid&#x60;
[**get_schema_by_id**](SchemaRegistryApi.md#get_schema_by_id) | **GET** /schema-registry/schemas/{guid} | Fetch the schema from the registry by &#x60;guid&#x60;
[**lookup_schemas_by_query**](SchemaRegistryApi.md#lookup_schemas_by_query) | **GET** /schema-registry/schemas | Lookup schemas by indexed fields
[**update_schema**](SchemaRegistryApi.md#update_schema) | **PUT** /schema-registry/{author}/{id} | Publish the new version of the credential schema to the schema registry

# **create_schema**
> CredentialSchemaResponse create_schema(body)

Publish new schema to the schema registry

Create the new credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchemaRegistryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CredentialSchemaInput() # CredentialSchemaInput | JSON object required for the credential schema creation

try:
    # Publish new schema to the schema registry
    api_response = api_instance.create_schema(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaRegistryApi->create_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialSchemaInput**](CredentialSchemaInput.md)| JSON object required for the credential schema creation | 

### Return type

[**CredentialSchemaResponse**](CredentialSchemaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_schema_by_id**
> object get_raw_schema_by_id(guid)

Fetch the schema from the registry by `guid`

Fetch the credential schema by the unique identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: adminApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-admin-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-admin-api-key'] = 'Bearer'
# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchemaRegistryApi(swagger_client.ApiClient(configuration))
guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch the schema from the registry by `guid`
    api_response = api_instance.get_raw_schema_by_id(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaRegistryApi->get_raw_schema_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_by_id**
> CredentialSchemaResponse get_schema_by_id(guid)

Fetch the schema from the registry by `guid`

Fetch the credential schema by the unique identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: adminApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-admin-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-admin-api-key'] = 'Bearer'
# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchemaRegistryApi(swagger_client.ApiClient(configuration))
guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Globally unique identifier of the credential schema record

try:
    # Fetch the schema from the registry by `guid`
    api_response = api_instance.get_schema_by_id(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaRegistryApi->get_schema_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| Globally unique identifier of the credential schema record | 

### Return type

[**CredentialSchemaResponse**](CredentialSchemaResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_schemas_by_query**
> CredentialSchemaResponsePage lookup_schemas_by_query(author=author, name=name, version=version, tags=tags, offset=offset, limit=limit, order=order)

Lookup schemas by indexed fields

Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and `limit` parameters 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchemaRegistryApi(swagger_client.ApiClient(configuration))
author = 'author_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
tags = 'tags_example' # str |  (optional)
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)
order = 'order_example' # str |  (optional)

try:
    # Lookup schemas by indexed fields
    api_response = api_instance.lookup_schemas_by_query(author=author, name=name, version=version, tags=tags, offset=offset, limit=limit, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaRegistryApi->lookup_schemas_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **tags** | **str**|  | [optional] 
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**CredentialSchemaResponsePage**](CredentialSchemaResponsePage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schema**
> CredentialSchemaResponse update_schema(body, author, id)

Publish the new version of the credential schema to the schema registry

Publish the new version of the credential schema record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential schema will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchemaRegistryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CredentialSchemaInput() # CredentialSchemaInput | JSON object required for the credential schema update
author = 'author_example' # str | DID of the identity which authored the credential schema. A piece of Metadata.
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A locally unique identifier to address the schema. UUID is generated by the backend.

try:
    # Publish the new version of the credential schema to the schema registry
    api_response = api_instance.update_schema(body, author, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaRegistryApi->update_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialSchemaInput**](CredentialSchemaInput.md)| JSON object required for the credential schema update | 
 **author** | **str**| DID of the identity which authored the credential schema. A piece of Metadata. | 
 **id** | [**str**](.md)| A locally unique identifier to address the schema. UUID is generated by the backend. | 

### Return type

[**CredentialSchemaResponse**](CredentialSchemaResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

