# swagger_client.DIDRegistrarApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_did_registrar_dids**](DIDRegistrarApi.md#get_did_registrar_dids) | **GET** /did-registrar/dids | List all DIDs stored in the agent&#x27;s wallet
[**get_did_registrar_dids_didref**](DIDRegistrarApi.md#get_did_registrar_dids_didref) | **GET** /did-registrar/dids/{didRef} | Get a specific DID stored in the agent&#x27;s wallet
[**post_did_registrar_dids**](DIDRegistrarApi.md#post_did_registrar_dids) | **POST** /did-registrar/dids | Create an unpublished PRISM DID and store it in the agent&#x27;s wallet
[**post_did_registrar_dids_didref_deactivations**](DIDRegistrarApi.md#post_did_registrar_dids_didref_deactivations) | **POST** /did-registrar/dids/{didRef}/deactivations | Deactivate DID in the agent&#x27;s wallet and post deactivate operation to the VDR
[**post_did_registrar_dids_didref_publications**](DIDRegistrarApi.md#post_did_registrar_dids_didref_publications) | **POST** /did-registrar/dids/{didRef}/publications | Publish the DID stored in the agent&#x27;s wallet to the VDR
[**post_did_registrar_dids_didref_updates**](DIDRegistrarApi.md#post_did_registrar_dids_didref_updates) | **POST** /did-registrar/dids/{didRef}/updates | Update DID in the agent&#x27;s wallet and post update operation to the VDR

# **get_did_registrar_dids**
> ManagedDIDPage get_did_registrar_dids(offset=offset, limit=limit)

List all DIDs stored in the agent's wallet

List all DIDs stored in the agent's wallet. Return a paginated items ordered by created timestamp.

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)

try:
    # List all DIDs stored in the agent's wallet
    api_response = api_instance.get_did_registrar_dids(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->get_did_registrar_dids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 

### Return type

[**ManagedDIDPage**](ManagedDIDPage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_did_registrar_dids_didref**
> ManagedDID get_did_registrar_dids_didref(did_ref)

Get a specific DID stored in the agent's wallet

Get a specific DID stored in the agent's wallet

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
did_ref = 'did_ref_example' # str | Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax)

try:
    # Get a specific DID stored in the agent's wallet
    api_response = api_instance.get_did_registrar_dids_didref(did_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->get_did_registrar_dids_didref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did_ref** | **str**| Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) | 

### Return type

[**ManagedDID**](ManagedDID.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_did_registrar_dids**
> CreateManagedDIDResponse post_did_registrar_dids(body)

Create an unpublished PRISM DID and store it in the agent's wallet

Create an unpublished PRISM DID and store it in the agent's wallet. The public/private keys of the DID will be derived according to the `didDocumentTemplate` and managed by the agent. The DID can later be published to the VDR using the `publications` endpoint. After the DID is created, it has the `CREATED` status.

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateManagedDidRequest() # CreateManagedDidRequest | 

try:
    # Create an unpublished PRISM DID and store it in the agent's wallet
    api_response = api_instance.post_did_registrar_dids(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->post_did_registrar_dids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateManagedDidRequest**](CreateManagedDidRequest.md)|  | 

### Return type

[**CreateManagedDIDResponse**](CreateManagedDIDResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_did_registrar_dids_didref_deactivations**
> DIDOperationResponse post_did_registrar_dids_didref_deactivations(did_ref)

Deactivate DID in the agent's wallet and post deactivate operation to the VDR

Deactivate DID in the agent's wallet and post deactivate operation to the VDR. Only the DID with status `PUBLISHED` can be deactivated. The deactivate operation is asynchornous operation and the agent will reject a new deactivate request if the previous operation is not yet comfirmed.

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
did_ref = 'did_ref_example' # str | Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax)

try:
    # Deactivate DID in the agent's wallet and post deactivate operation to the VDR
    api_response = api_instance.post_did_registrar_dids_didref_deactivations(did_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->post_did_registrar_dids_didref_deactivations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did_ref** | **str**| Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) | 

### Return type

[**DIDOperationResponse**](DIDOperationResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_did_registrar_dids_didref_publications**
> DIDOperationResponse post_did_registrar_dids_didref_publications(did_ref)

Publish the DID stored in the agent's wallet to the VDR

Initiate the publication of the DID stored in the agent's wallet to the VDR. The publishing process is asynchronous. Attempting to publish the same DID while the previous publication is ongoing will not initiate another publication. After the submission of the DID publication, its status is changed to `PUBLICATION_PENDING`. Upon confirmation after a predefined number of blocks, the status is changed to `PUBLISHED`. In case of a failed DID publication, the status is reverted to `CREATED`. 

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
did_ref = 'did_ref_example' # str | Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax)

try:
    # Publish the DID stored in the agent's wallet to the VDR
    api_response = api_instance.post_did_registrar_dids_didref_publications(did_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->post_did_registrar_dids_didref_publications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did_ref** | **str**| Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) | 

### Return type

[**DIDOperationResponse**](DIDOperationResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_did_registrar_dids_didref_updates**
> DIDOperationResponse post_did_registrar_dids_didref_updates(body, did_ref)

Update DID in the agent's wallet and post update operation to the VDR

Update DID in the agent's wallet and post the update operation to the VDR. Only the DID with status `PUBLISHED` can be updated. This endpoint updates the DID document from the last confirmed operation. The update operation is asynchornous operation and the agent will reject a new update request if the previous operation is not yet comfirmed.

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
api_instance = swagger_client.DIDRegistrarApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateManagedDIDRequest() # UpdateManagedDIDRequest | 
did_ref = 'did_ref_example' # str | Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax)

try:
    # Update DID in the agent's wallet and post update operation to the VDR
    api_response = api_instance.post_did_registrar_dids_didref_updates(body, did_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DIDRegistrarApi->post_did_registrar_dids_didref_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateManagedDIDRequest**](UpdateManagedDIDRequest.md)|  | 
 **did_ref** | **str**| Prism DID according to [the Prism DID method syntax](https://github.com/input-output-hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#prism-did-method-syntax) | 

### Return type

[**DIDOperationResponse**](DIDOperationResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

