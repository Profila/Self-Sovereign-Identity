# swagger_client.DIDApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_did**](DIDApi.md#get_did) | **GET** /dids/{didRef} | Resolve Prism DID to a W3C representation

# **get_did**
> DIDResolutionResult get_did(did_ref)

Resolve Prism DID to a W3C representation

Resolve Prism DID to a W3C DID document representation. The response can be the [DID resolution result](https://w3c-ccg.github.io/did-resolution/#did-resolution-result) or [DID document representation](https://www.w3.org/TR/did-core/#representations) depending on the `Accept` request header. The response is implemented according to [resolver HTTP binding](https://w3c-ccg.github.io/did-resolution/#bindings-https) in the DID resolution spec. 

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
api_instance = swagger_client.DIDApi(swagger_client.ApiClient(configuration))
did_ref = 'did_ref_example' # str | Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax)

try:
    # Resolve Prism DID to a W3C representation
    api_response = api_instance.get_did(did_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDApi->get_did: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did_ref** | **str**| Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) | 

### Return type

[**DIDResolutionResult**](DIDResolutionResult.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json; profile=https://w3id.org/did-resolution, application/did+ld+json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

