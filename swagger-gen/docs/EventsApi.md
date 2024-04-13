# swagger_client.EventsApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_events_webhooks_id**](EventsApi.md#delete_events_webhooks_id) | **DELETE** /events/webhooks/{id} | Delete the wallet webhook notification by &#x60;id&#x60;
[**get_events_webhooks**](EventsApi.md#get_events_webhooks) | **GET** /events/webhooks | List wallet webhook notifications
[**post_events_webhooks**](EventsApi.md#post_events_webhooks) | **POST** /events/webhooks | Create wallet webhook notifications

# **delete_events_webhooks_id**
> delete_events_webhooks_id(id)

Delete the wallet webhook notification by `id`

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the webhook notification to delete.

try:
    # Delete the wallet webhook notification by `id`
    api_instance.delete_events_webhooks_id(id)
except ApiException as e:
    print("Exception when calling EventsApi->delete_events_webhooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID of the webhook notification to delete. | 

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_webhooks**
> WebhookNotificationPage get_events_webhooks()

List wallet webhook notifications

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))

try:
    # List wallet webhook notifications
    api_response = api_instance.get_events_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhookNotificationPage**](WebhookNotificationPage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_events_webhooks**
> WebhookNotification post_events_webhooks(body)

Create wallet webhook notifications

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
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWebhookNotification() # CreateWebhookNotification | 

try:
    # Create wallet webhook notifications
    api_response = api_instance.post_events_webhooks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->post_events_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebhookNotification**](CreateWebhookNotification.md)|  | 

### Return type

[**WebhookNotification**](WebhookNotification.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

