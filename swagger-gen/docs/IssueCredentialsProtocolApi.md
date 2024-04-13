# swagger_client.IssueCredentialsProtocolApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_credential_offer**](IssueCredentialsProtocolApi.md#accept_credential_offer) | **POST** /issue-credentials/records/{recordId}/accept-offer | As a holder, accept a new credential offer received from another issuer Agent.
[**create_credential_offer**](IssueCredentialsProtocolApi.md#create_credential_offer) | **POST** /issue-credentials/credential-offers | As a credential issuer, create a new credential offer that will be sent to a holder Agent.
[**get_credential_record**](IssueCredentialsProtocolApi.md#get_credential_record) | **GET** /issue-credentials/records/{recordId} | Retrieves a specific issue credential flow record from the Agent&#x27;s database based on its unique &#x60;recordId&#x60;.
[**get_credential_records**](IssueCredentialsProtocolApi.md#get_credential_records) | **GET** /issue-credentials/records | Retrieves the list of issue credential records from the Agent&#x27;s database.
[**issue_credential**](IssueCredentialsProtocolApi.md#issue_credential) | **POST** /issue-credentials/records/{recordId}/issue-credential | As an issuer, issues the verifiable credential related the identified issuance flow record.

# **accept_credential_offer**
> IssueCredentialRecord accept_credential_offer(body, record_id)

As a holder, accept a new credential offer received from another issuer Agent.

 As a holder, accept a new credential offer received from an issuer Agent. The subsequent credential request message sent to the issuer adheres to the [Issue Credential Protocol 3.0 - Request Credential](https://github.com/decentralized-identity/waci-didcomm/tree/main/issue_credential#request-credential) specification. 

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
api_instance = swagger_client.IssueCredentialsProtocolApi(swagger_client.ApiClient(configuration))
body = swagger_client.AcceptCredentialOfferRequest() # AcceptCredentialOfferRequest | The accept credential offer request object.
record_id = 'record_id_example' # str | The `recordId` uniquely identifying the issue credential flow record.

try:
    # As a holder, accept a new credential offer received from another issuer Agent.
    api_response = api_instance.accept_credential_offer(body, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialsProtocolApi->accept_credential_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AcceptCredentialOfferRequest**](AcceptCredentialOfferRequest.md)| The accept credential offer request object. | 
 **record_id** | **str**| The &#x60;recordId&#x60; uniquely identifying the issue credential flow record. | 

### Return type

[**IssueCredentialRecord**](IssueCredentialRecord.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credential_offer**
> IssueCredentialRecord create_credential_offer(body)

As a credential issuer, create a new credential offer that will be sent to a holder Agent.

 Creates a new credential offer that will be delivered, through a previously established DIDComm connection, to a holder Agent. The subsequent credential offer message adheres to the [Issue Credential Protocol 3.0 - Offer Credential](https://github.com/decentralized-identity/waci-didcomm/tree/main/issue_credential#offer-credential) specification. The created offer can be of two types: 'JWT' or 'AnonCreds'. 

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
api_instance = swagger_client.IssueCredentialsProtocolApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateIssueCredentialRecordRequest() # CreateIssueCredentialRecordRequest | The credential offer object.

try:
    # As a credential issuer, create a new credential offer that will be sent to a holder Agent.
    api_response = api_instance.create_credential_offer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialsProtocolApi->create_credential_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIssueCredentialRecordRequest**](CreateIssueCredentialRecordRequest.md)| The credential offer object. | 

### Return type

[**IssueCredentialRecord**](IssueCredentialRecord.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_record**
> IssueCredentialRecord get_credential_record(record_id)

Retrieves a specific issue credential flow record from the Agent's database based on its unique `recordId`.

 Retrieves a specific issue credential flow record from the Agent's database based on its unique `recordId`. The API returns a comprehensive collection of issue credential flow records within the system, regardless of their state. The returned items include essential metadata such as record ID, thread ID, state, role, issued credential, and other relevant details. 

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
api_instance = swagger_client.IssueCredentialsProtocolApi(swagger_client.ApiClient(configuration))
record_id = 'record_id_example' # str | The `recordId` uniquely identifying the issue credential flow record.

try:
    # Retrieves a specific issue credential flow record from the Agent's database based on its unique `recordId`.
    api_response = api_instance.get_credential_record(record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialsProtocolApi->get_credential_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**| The &#x60;recordId&#x60; uniquely identifying the issue credential flow record. | 

### Return type

[**IssueCredentialRecord**](IssueCredentialRecord.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_records**
> IssueCredentialRecordPage get_credential_records(offset=offset, limit=limit, thid=thid)

Retrieves the list of issue credential records from the Agent's database.

 Retrieves the list of issue credential records from the Agent's database. The API returns a comprehensive collection of issue credential flow records within the system, regardless of their state. The returned items include essential metadata such as record ID, thread ID, state, role, issued credential, and other relevant details. 

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
api_instance = swagger_client.IssueCredentialsProtocolApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)
thid = 'thid_example' # str | The thread ID associated with a specific credential issue flow execution. (optional)

try:
    # Retrieves the list of issue credential records from the Agent's database.
    api_response = api_instance.get_credential_records(offset=offset, limit=limit, thid=thid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialsProtocolApi->get_credential_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 
 **thid** | **str**| The thread ID associated with a specific credential issue flow execution. | [optional] 

### Return type

[**IssueCredentialRecordPage**](IssueCredentialRecordPage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential**
> IssueCredentialRecord issue_credential(record_id)

As an issuer, issues the verifiable credential related the identified issuance flow record.

 As an issuer, issues the verifiable credential related the identified issuance flow record. The JWT or AnonCreds credential will be generated and sent to the holder Agent asynchronously and through DIDComm. Note that this endpoint should only be called when automatic issuance is disabled for this record (i.e. `automaticIssuance` attribute set to `false` at offer creation time). 

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
api_instance = swagger_client.IssueCredentialsProtocolApi(swagger_client.ApiClient(configuration))
record_id = 'record_id_example' # str | The `recordId` uniquely identifying the issue credential flow record.

try:
    # As an issuer, issues the verifiable credential related the identified issuance flow record.
    api_response = api_instance.issue_credential(record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialsProtocolApi->issue_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**| The &#x60;recordId&#x60; uniquely identifying the issue credential flow record. | 

### Return type

[**IssueCredentialRecord**](IssueCredentialRecord.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

