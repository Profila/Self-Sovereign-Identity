# swagger_client.PresentProofApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_presentation**](PresentProofApi.md#get_all_presentation) | **GET** /present-proof/presentations | Gets the list of proof presentation records.
[**get_presentation**](PresentProofApi.md#get_presentation) | **GET** /present-proof/presentations/{presentationId} | Gets an existing proof presentation record by its unique identifier. More information on the error can be found in the response body.
[**request_presentation**](PresentProofApi.md#request_presentation) | **POST** /present-proof/presentations | As a Verifier, create a new proof presentation request and send it to the Prover.
[**update_presentation**](PresentProofApi.md#update_presentation) | **PATCH** /present-proof/presentations/{presentationId} | Updates the proof presentation record matching the unique identifier, with the specific action to perform.

# **get_all_presentation**
> PresentationStatusPage get_all_presentation(offset=offset, limit=limit, thid=thid)

Gets the list of proof presentation records.

list of presentation statuses

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
api_instance = swagger_client.PresentProofApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)
thid = 'thid_example' # str |  (optional)

try:
    # Gets the list of proof presentation records.
    api_response = api_instance.get_all_presentation(offset=offset, limit=limit, thid=thid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->get_all_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 
 **thid** | **str**|  | [optional] 

### Return type

[**PresentationStatusPage**](PresentationStatusPage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presentation**
> PresentationStatus get_presentation(presentation_id)

Gets an existing proof presentation record by its unique identifier. More information on the error can be found in the response body.

Returns an existing presentation record by id.

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
api_instance = swagger_client.PresentProofApi(swagger_client.ApiClient(configuration))
presentation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the presentation record.

try:
    # Gets an existing proof presentation record by its unique identifier. More information on the error can be found in the response body.
    api_response = api_instance.get_presentation(presentation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->get_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presentation_id** | [**str**](.md)| The unique identifier of the presentation record. | 

### Return type

[**PresentationStatus**](PresentationStatus.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_presentation**
> PresentationStatus request_presentation(body)

As a Verifier, create a new proof presentation request and send it to the Prover.

Holder presents proof derived from the verifiable credential to verifier.

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
api_instance = swagger_client.PresentProofApi(swagger_client.ApiClient(configuration))
body = swagger_client.RequestPresentationInput() # RequestPresentationInput | The present proof creation request.

try:
    # As a Verifier, create a new proof presentation request and send it to the Prover.
    api_response = api_instance.request_presentation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->request_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPresentationInput**](RequestPresentationInput.md)| The present proof creation request. | 

### Return type

[**PresentationStatus**](PresentationStatus.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_presentation**
> PresentationStatus update_presentation(body, presentation_id)

Updates the proof presentation record matching the unique identifier, with the specific action to perform.

Accept or reject presentation of proof request.

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
api_instance = swagger_client.PresentProofApi(swagger_client.ApiClient(configuration))
body = swagger_client.RequestPresentationAction() # RequestPresentationAction | The action to perform on the proof presentation record.
presentation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the presentation record.

try:
    # Updates the proof presentation record matching the unique identifier, with the specific action to perform.
    api_response = api_instance.update_presentation(body, presentation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPresentationAction**](RequestPresentationAction.md)| The action to perform on the proof presentation record. | 
 **presentation_id** | [**str**](.md)| The unique identifier of the presentation record. | 

### Return type

[**PresentationStatus**](PresentationStatus.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

