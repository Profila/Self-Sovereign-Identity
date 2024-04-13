# swagger_client.CredentialStatusListApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credential_status_list_endpoint**](CredentialStatusListApi.md#get_credential_status_list_endpoint) | **GET** /credential-status/{id} | Fetch credential status list by its ID
[**patch_credential_status_revoke_credential_id**](CredentialStatusListApi.md#patch_credential_status_revoke_credential_id) | **PATCH** /credential-status/revoke-credential/{id} | Revoke a credential by its ID

# **get_credential_status_list_endpoint**
> StatusListCredential get_credential_status_list_endpoint(id)

Fetch credential status list by its ID

Fetch credential status list by its ID

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
api_instance = swagger_client.CredentialStatusListApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Globally unique identifier of the credential status list

try:
    # Fetch credential status list by its ID
    api_response = api_instance.get_credential_status_list_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialStatusListApi->get_credential_status_list_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Globally unique identifier of the credential status list | 

### Return type

[**StatusListCredential**](StatusListCredential.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_credential_status_revoke_credential_id**
> patch_credential_status_revoke_credential_id(id)

Revoke a credential by its ID

Marks credential to be ready for revocation, it will be revoked automatically

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
api_instance = swagger_client.CredentialStatusListApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Revoke a credential by its ID

try:
    # Revoke a credential by its ID
    api_instance.patch_credential_status_revoke_credential_id(id)
except ApiException as e:
    print("Exception when calling CredentialStatusListApi->patch_credential_status_revoke_credential_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Revoke a credential by its ID | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

