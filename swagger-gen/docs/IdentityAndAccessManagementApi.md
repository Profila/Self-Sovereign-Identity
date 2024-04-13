# swagger_client.IdentityAndAccessManagementApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entity_api_key_authentication**](IdentityAndAccessManagementApi.md#add_entity_api_key_authentication) | **POST** /iam/apikey-authentication | Register the &#x60;apikey&#x60; for the entity
[**create_entity**](IdentityAndAccessManagementApi.md#create_entity) | **POST** /iam/entities | Create a new entity record
[**delete_entity_api_key_authentication**](IdentityAndAccessManagementApi.md#delete_entity_api_key_authentication) | **DELETE** /iam/apikey-authentication | Unregister the &#x60;apikey&#x60; for the entity
[**delete_entity_by_id**](IdentityAndAccessManagementApi.md#delete_entity_by_id) | **DELETE** /iam/entities/{id} | Delete the entity by &#x60;id&#x60;
[**get_all_entities**](IdentityAndAccessManagementApi.md#get_all_entities) | **GET** /iam/entities | Get all entities
[**get_entity_by_id**](IdentityAndAccessManagementApi.md#get_entity_by_id) | **GET** /iam/entities/{id} | Get the entity by the &#x60;id&#x60;
[**update_entity_name**](IdentityAndAccessManagementApi.md#update_entity_name) | **PUT** /iam/entities/{id}/name | Update the entity record name by &#x60;id&#x60;
[**update_entity_wallet_id**](IdentityAndAccessManagementApi.md#update_entity_wallet_id) | **PUT** /iam/entities/{id}/walletId | Update the entity record &#x60;walletId&#x60; by &#x60;id&#x60;

# **add_entity_api_key_authentication**
> add_entity_api_key_authentication(body)

Register the `apikey` for the entity

Register the `apikey` for the entity.

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiKeyAuthenticationRequest() # ApiKeyAuthenticationRequest | JSON object required for the registering the entity and `apikey`

try:
    # Register the `apikey` for the entity
    api_instance.add_entity_api_key_authentication(body)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->add_entity_api_key_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyAuthenticationRequest**](ApiKeyAuthenticationRequest.md)| JSON object required for the registering the entity and &#x60;apikey&#x60; | 

### Return type

void (empty response body)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> EntityResponse create_entity(body)

Create a new entity record

Create the new entity record. The entity record is a representation of the account in the system.

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateEntityRequest() # CreateEntityRequest | JSON object required for the entity creation

try:
    # Create a new entity record
    api_response = api_instance.create_entity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntityRequest**](CreateEntityRequest.md)| JSON object required for the entity creation | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_api_key_authentication**
> delete_entity_api_key_authentication(body)

Unregister the `apikey` for the entity

Unregister the `apikey` for the entity.

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiKeyAuthenticationRequest() # ApiKeyAuthenticationRequest | JSON object required for the unregistering the entity and `apikey`

try:
    # Unregister the `apikey` for the entity
    api_instance.delete_entity_api_key_authentication(body)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->delete_entity_api_key_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyAuthenticationRequest**](ApiKeyAuthenticationRequest.md)| JSON object required for the unregistering the entity and &#x60;apikey&#x60; | 

### Return type

void (empty response body)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_by_id**
> delete_entity_by_id(id)

Delete the entity by `id`

Delete the entity by the unique identifier

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifier of the entity

try:
    # Delete the entity by `id`
    api_instance.delete_entity_by_id(id)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->delete_entity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Identifier of the entity | 

### Return type

void (empty response body)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_entities**
> EntityResponsePage get_all_entities(offset=offset, limit=limit)

Get all entities

Get all entities with the pagination by `offset` and `limit` parameters 

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)

try:
    # Get all entities
    api_response = api_instance.get_all_entities(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->get_all_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 

### Return type

[**EntityResponsePage**](EntityResponsePage.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_by_id**
> EntityResponse get_entity_by_id(id)

Get the entity by the `id`

Get the entity by the unique identifier

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifier of the entity

try:
    # Get the entity by the `id`
    api_response = api_instance.get_entity_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->get_entity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Identifier of the entity | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_name**
> EntityResponse update_entity_name(body, id)

Update the entity record name by `id`

Update the entity record name by `id`

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateEntityNameRequest() # UpdateEntityNameRequest | JSON object required for the entity name update
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update the entity record name by `id`
    api_response = api_instance.update_entity_name(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->update_entity_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEntityNameRequest**](UpdateEntityNameRequest.md)| JSON object required for the entity name update | 
 **id** | [**str**](.md)|  | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_wallet_id**
> EntityResponse update_entity_wallet_id(body, id)

Update the entity record `walletId` by `id`

Update the entity record `walletId` field by `id`

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

# create an instance of the API class
api_instance = swagger_client.IdentityAndAccessManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateEntityWalletIdRequest() # UpdateEntityWalletIdRequest | JSON object required for the entity walletId update
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update the entity record `walletId` by `id`
    api_response = api_instance.update_entity_wallet_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityAndAccessManagementApi->update_entity_wallet_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEntityWalletIdRequest**](UpdateEntityWalletIdRequest.md)| JSON object required for the entity walletId update | 
 **id** | [**str**](.md)|  | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[adminApiKeyAuth](../README.md#adminApiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

