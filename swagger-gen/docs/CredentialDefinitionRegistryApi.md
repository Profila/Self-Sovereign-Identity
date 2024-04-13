# swagger_client.CredentialDefinitionRegistryApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential_definition**](CredentialDefinitionRegistryApi.md#create_credential_definition) | **POST** /credential-definition-registry/definitions | Publish new definition to the definition registry
[**get_credential_definition_by_id**](CredentialDefinitionRegistryApi.md#get_credential_definition_by_id) | **GET** /credential-definition-registry/definitions/{guid} | Fetch the credential definition from the registry by &#x60;guid&#x60;
[**get_credential_definition_inner_definition_by_id**](CredentialDefinitionRegistryApi.md#get_credential_definition_inner_definition_by_id) | **GET** /credential-definition-registry/definitions/{guid}/definition | Fetch the inner definition field of the credential definition from the registry by &#x60;guid&#x60;
[**lookup_credential_definitions_by_query**](CredentialDefinitionRegistryApi.md#lookup_credential_definitions_by_query) | **GET** /credential-definition-registry/definitions | Lookup credential definitions by indexed fields

# **create_credential_definition**
> CredentialDefinitionResponse create_credential_definition(body)

Publish new definition to the definition registry

Create the new credential definition record with metadata and internal JSON Schema on behalf of Cloud Agent. The credential definition will be signed by the keys of Cloud Agent and issued by the DID that corresponds to it.

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
api_instance = swagger_client.CredentialDefinitionRegistryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CredentialDefinitionInput() # CredentialDefinitionInput | JSON object required for the credential definition creation

try:
    # Publish new definition to the definition registry
    api_response = api_instance.create_credential_definition(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionRegistryApi->create_credential_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialDefinitionInput**](CredentialDefinitionInput.md)| JSON object required for the credential definition creation | 

### Return type

[**CredentialDefinitionResponse**](CredentialDefinitionResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_definition_by_id**
> CredentialDefinitionResponse get_credential_definition_by_id(guid)

Fetch the credential definition from the registry by `guid`

Fetch the credential definition by the unique identifier

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
api_instance = swagger_client.CredentialDefinitionRegistryApi(swagger_client.ApiClient(configuration))
guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Globally unique identifier of the credential definition record

try:
    # Fetch the credential definition from the registry by `guid`
    api_response = api_instance.get_credential_definition_by_id(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionRegistryApi->get_credential_definition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| Globally unique identifier of the credential definition record | 

### Return type

[**CredentialDefinitionResponse**](CredentialDefinitionResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_definition_inner_definition_by_id**
> object get_credential_definition_inner_definition_by_id(guid)

Fetch the inner definition field of the credential definition from the registry by `guid`

Fetch the inner definition fields of the credential definition by the unique identifier

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
api_instance = swagger_client.CredentialDefinitionRegistryApi(swagger_client.ApiClient(configuration))
guid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch the inner definition field of the credential definition from the registry by `guid`
    api_response = api_instance.get_credential_definition_inner_definition_by_id(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionRegistryApi->get_credential_definition_inner_definition_by_id: %s\n" % e)
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

# **lookup_credential_definitions_by_query**
> CredentialDefinitionResponsePage lookup_credential_definitions_by_query(author=author, name=name, version=version, tag=tag, offset=offset, limit=limit, order=order)

Lookup credential definitions by indexed fields

Lookup credential definitions by `author`, `name`, `tag` parameters and control the pagination by `offset` and `limit` parameters 

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
api_instance = swagger_client.CredentialDefinitionRegistryApi(swagger_client.ApiClient(configuration))
author = 'author_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)
order = 'order_example' # str |  (optional)

try:
    # Lookup credential definitions by indexed fields
    api_response = api_instance.lookup_credential_definitions_by_query(author=author, name=name, version=version, tag=tag, offset=offset, limit=limit, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialDefinitionRegistryApi->lookup_credential_definitions_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**CredentialDefinitionResponsePage**](CredentialDefinitionResponsePage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

