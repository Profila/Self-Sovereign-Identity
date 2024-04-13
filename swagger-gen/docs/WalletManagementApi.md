# swagger_client.WalletManagementApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet**](WalletManagementApi.md#create_wallet) | **POST** /wallets | Create a new wallet
[**create_wallet_uma_permission**](WalletManagementApi.md#create_wallet_uma_permission) | **POST** /wallets/{walletId}/uma-permissions | Create a UMA resource permission on an authorization server for the wallet.
[**delete_wallet_uma_permission**](WalletManagementApi.md#delete_wallet_uma_permission) | **DELETE** /wallets/{walletId}/uma-permissions | Delete a UMA resource permission on an authorization server for the wallet.
[**get_wallets**](WalletManagementApi.md#get_wallets) | **GET** /wallets | List all permitted wallets
[**get_wallets_walletid**](WalletManagementApi.md#get_wallets_walletid) | **GET** /wallets/{walletId} | Get the wallet by ID

# **create_wallet**
> WalletDetail create_wallet(body)

Create a new wallet

Create a new wallet with the option to provide the seed. The seed will be used for all PRISM DID keypair derivation within the wallet.  If the role is admin, a wallet can be created at any time. If the role is tenant, a wallet can only be created if there is no existing wallet permission for that tenant. The permission for the tenant will be automatically granted after the wallet is created with tenant role.         

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
api_instance = swagger_client.WalletManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWalletRequest() # CreateWalletRequest | 

try:
    # Create a new wallet
    api_response = api_instance.create_wallet(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletManagementApi->create_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWalletRequest**](CreateWalletRequest.md)|  | 

### Return type

[**WalletDetail**](WalletDetail.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_uma_permission**
> create_wallet_uma_permission(body, wallet_id)

Create a UMA resource permission on an authorization server for the wallet.

Create a UMA resource permission on an authorization server for the wallet. This grants the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.           

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
api_instance = swagger_client.WalletManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWalletUmaPermissionRequest() # CreateWalletUmaPermissionRequest | 
wallet_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Create a UMA resource permission on an authorization server for the wallet.
    api_instance.create_wallet_uma_permission(body, wallet_id)
except ApiException as e:
    print("Exception when calling WalletManagementApi->create_wallet_uma_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWalletUmaPermissionRequest**](CreateWalletUmaPermissionRequest.md)|  | 
 **wallet_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wallet_uma_permission**
> delete_wallet_uma_permission(wallet_id, subject)

Delete a UMA resource permission on an authorization server for the wallet.

Remove a UMA resource permission on an authorization server for the wallet. This remove the wallet permission to the specified `subject`, where the `subject` denotes the identity of the tenant on an authorization server.           

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
api_instance = swagger_client.WalletManagementApi(swagger_client.ApiClient(configuration))
wallet_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
subject = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a UMA resource permission on an authorization server for the wallet.
    api_instance.delete_wallet_uma_permission(wallet_id, subject)
except ApiException as e:
    print("Exception when calling WalletManagementApi->delete_wallet_uma_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | [**str**](.md)|  | 
 **subject** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallets**
> WalletDetailPage get_wallets(offset=offset, limit=limit)

List all permitted wallets

List all permitted wallets. If the role is admin, returns all the wallets. If the role is tenant, only return permitted wallets.

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
api_instance = swagger_client.WalletManagementApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)

try:
    # List all permitted wallets
    api_response = api_instance.get_wallets(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletManagementApi->get_wallets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 

### Return type

[**WalletDetailPage**](WalletDetailPage.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallets_walletid**
> WalletDetail get_wallets_walletid(wallet_id)

Get the wallet by ID

Get the wallet by ID. If the role is tenant, only search the ID of permitted wallets.

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
api_instance = swagger_client.WalletManagementApi(swagger_client.ApiClient(configuration))
wallet_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get the wallet by ID
    api_response = api_instance.get_wallets_walletid(wallet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletManagementApi->get_wallets_walletid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | [**str**](.md)|  | 

### Return type

[**WalletDetail**](WalletDetail.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

