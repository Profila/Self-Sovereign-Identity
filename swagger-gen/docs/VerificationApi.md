# swagger_client.VerificationApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification_policy**](VerificationApi.md#create_verification_policy) | **POST** /verification/policies | Create the new verification policy
[**delete_verification_policy_by_id**](VerificationApi.md#delete_verification_policy_by_id) | **DELETE** /verification/policies/{id} | Deleted the verification policy by id
[**get_verification_policy_by_id**](VerificationApi.md#get_verification_policy_by_id) | **GET** /verification/policies/{id} | Fetch the verification policy by id
[**lookup_verification_policies_by_query**](VerificationApi.md#lookup_verification_policies_by_query) | **GET** /verification/policies | Lookup verification policies by query
[**update_verification_policy**](VerificationApi.md#update_verification_policy) | **PUT** /verification/policies/{id} | Update the verification policy object by id

# **create_verification_policy**
> VerificationPolicyResponse create_verification_policy(body)

Create the new verification policy

Create the new verification policy

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
api_instance = swagger_client.VerificationApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificationPolicyInput() # VerificationPolicyInput | Create verification policy object

try:
    # Create the new verification policy
    api_response = api_instance.create_verification_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->create_verification_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificationPolicyInput**](VerificationPolicyInput.md)| Create verification policy object | 

### Return type

[**VerificationPolicyResponse**](VerificationPolicyResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_verification_policy_by_id**
> delete_verification_policy_by_id(id)

Deleted the verification policy by id

Delete the verification policy by id

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
api_instance = swagger_client.VerificationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Delete the verification policy by id

try:
    # Deleted the verification policy by id
    api_instance.delete_verification_policy_by_id(id)
except ApiException as e:
    print("Exception when calling VerificationApi->delete_verification_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Delete the verification policy by id | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verification_policy_by_id**
> VerificationPolicyResponse get_verification_policy_by_id(id)

Fetch the verification policy by id

Get the verification policy by id

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
api_instance = swagger_client.VerificationApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Get the verification policy by id

try:
    # Fetch the verification policy by id
    api_response = api_instance.get_verification_policy_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->get_verification_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Get the verification policy by id | 

### Return type

[**VerificationPolicyResponse**](VerificationPolicyResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_verification_policies_by_query**
> VerificationPolicyResponsePage lookup_verification_policies_by_query(name=name, offset=offset, limit=limit, order=order)

Lookup verification policies by query

Lookup verification policies by `name`, and control the pagination by `offset` and `limit` parameters

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
api_instance = swagger_client.VerificationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | A human-readable name for the verification policy. The `name` cannot be empty. (optional)
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)
order = 'order_example' # str |  (optional)

try:
    # Lookup verification policies by query
    api_response = api_instance.lookup_verification_policies_by_query(name=name, offset=offset, limit=limit, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->lookup_verification_policies_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A human-readable name for the verification policy. The &#x60;name&#x60; cannot be empty. | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**VerificationPolicyResponsePage**](VerificationPolicyResponsePage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_verification_policy**
> VerificationPolicyResponse update_verification_policy(body, nonce, id)

Update the verification policy object by id

Update the verification policy entry

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
api_instance = swagger_client.VerificationApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerificationPolicyInput() # VerificationPolicyInput | Update verification policy object
nonce = 56 # int | Nonce of the previous VerificationPolicy
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update the verification policy object by id
    api_response = api_instance.update_verification_policy(body, nonce, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->update_verification_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerificationPolicyInput**](VerificationPolicyInput.md)| Update verification policy object | 
 **nonce** | **int**| Nonce of the previous VerificationPolicy | 
 **id** | [**str**](.md)|  | 

### Return type

[**VerificationPolicyResponse**](VerificationPolicyResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

