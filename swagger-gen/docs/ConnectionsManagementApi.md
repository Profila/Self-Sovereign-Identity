# swagger_client.ConnectionsManagementApi

All URIs are relative to *http://localhost:8085*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_connection_invitation**](ConnectionsManagementApi.md#accept_connection_invitation) | **POST** /connection-invitations | Accept a new connection invitation received out-of-band from another peer Agent.
[**create_connection**](ConnectionsManagementApi.md#create_connection) | **POST** /connections | Create a new connection invitation that can be delivered out-of-band to a peer Agent.
[**get_connection**](ConnectionsManagementApi.md#get_connection) | **GET** /connections/{connectionId} | Retrieves a specific connection flow record from the Agent&#x27;s database based on its unique &#x60;connectionId&#x60;.
[**get_connections**](ConnectionsManagementApi.md#get_connections) | **GET** /connections | Retrieves the list of connection flow records available from the Agent&#x27;s database.

# **accept_connection_invitation**
> Connection accept_connection_invitation(body)

Accept a new connection invitation received out-of-band from another peer Agent.

 Accept an new connection invitation received out-of-band from another peer Agent. The invitation must be compliant with the DIDComm Messaging v2.0 - [Out of Band Messages](https://identity.foundation/didcomm-messaging/spec/v2.0/#out-of-band-messages) specification [section 9.5.4](https://identity.foundation/didcomm-messaging/spec/v2.0/#invitation). A new connection record with state `ConnectionRequestPending` will be created in the agent database and later processed by a background job to send a connection request to the peer Agent. The created record will contain a newly generated pairwise Peer DID used for that connection. A connection request will then be sent to the peer Agent to actually establish the connection, moving the record state to `ConnectionRequestSent`, and waiting the connection response from the peer Agent. 

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
api_instance = swagger_client.ConnectionsManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.AcceptConnectionInvitationRequest() # AcceptConnectionInvitationRequest | The request used by an invitee to accept a connection invitation received from an inviter, using out-of-band mechanism.

try:
    # Accept a new connection invitation received out-of-band from another peer Agent.
    api_response = api_instance.accept_connection_invitation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsManagementApi->accept_connection_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AcceptConnectionInvitationRequest**](AcceptConnectionInvitationRequest.md)| The request used by an invitee to accept a connection invitation received from an inviter, using out-of-band mechanism. | 

### Return type

[**Connection**](Connection.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> Connection create_connection(body)

Create a new connection invitation that can be delivered out-of-band to a peer Agent.

 Create a new connection invitation that can be delivered out-of-band to a peer Agent, regardless of whether it resides in Cloud Agent or edge environment. The generated invitation adheres to the DIDComm Messaging v2.0 - [Out of Band Messages](https://identity.foundation/didcomm-messaging/spec/v2.0/#out-of-band-messages) specification [section 9.5.4](https://identity.foundation/didcomm-messaging/spec/v2.0/#invitation). The <b>from</b> field of the out-of-band invitation message contains a freshly generated Peer DID that complies with the [did:peer:2](https://identity.foundation/peer-did-method-spec/#generating-a-didpeer2) specification. This Peer DID includes the 'uri' location of the DIDComm messaging service, essential for the invitee's subsequent execution of the connection flow. In the Agent database, the created connection record has an initial state set to `InvitationGenerated`. The request body may contain a `label` that can be used as a human readable alias for the connection, for example `{'label': \"Connection with Bob\"}` 

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
api_instance = swagger_client.ConnectionsManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConnectionRequest() # CreateConnectionRequest | JSON object required for the connection creation.

try:
    # Create a new connection invitation that can be delivered out-of-band to a peer Agent.
    api_response = api_instance.create_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsManagementApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConnectionRequest**](CreateConnectionRequest.md)| JSON object required for the connection creation. | 

### Return type

[**Connection**](Connection.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> Connection get_connection(connection_id)

Retrieves a specific connection flow record from the Agent's database based on its unique `connectionId`.

 Retrieve a specific connection flow record from the Agent's database based in its unique `connectionId`. The returned item includes essential metadata such as connection ID, thread ID, state, role, participant information, and other relevant details. 

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
api_instance = swagger_client.ConnectionsManagementApi(swagger_client.ApiClient(configuration))
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The `connectionId` uniquely identifying the connection flow record.

try:
    # Retrieves a specific connection flow record from the Agent's database based on its unique `connectionId`.
    api_response = api_instance.get_connection(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsManagementApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**str**](.md)| The &#x60;connectionId&#x60; uniquely identifying the connection flow record. | 

### Return type

[**Connection**](Connection.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> ConnectionsPage get_connections(offset=offset, limit=limit, thid=thid)

Retrieves the list of connection flow records available from the Agent's database.

 Retrieve of a list containing connections available from the Agent's database. The API returns a comprehensive collection of connection flow records within the system, regardless of their state. Each connection item includes essential metadata such as connection ID, thread ID, state, role, participant information, and other relevant details. Pagination support is available, allowing for efficient handling of large datasets. 

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
api_instance = swagger_client.ConnectionsManagementApi(swagger_client.ApiClient(configuration))
offset = 56 # int | The number of items to skip before returning results. Default is 0 if not specified. (optional)
limit = 56 # int | The maximum number of items to return. Defaults to 100 if not specified. (optional)
thid = 'thid_example' # str | The `thid`, shared between the inviter and the invitee, that uniquely identifies a connection flow. (optional)

try:
    # Retrieves the list of connection flow records available from the Agent's database.
    api_response = api_instance.get_connections(offset=offset, limit=limit, thid=thid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsManagementApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before returning results. Default is 0 if not specified. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 100 if not specified. | [optional] 
 **thid** | **str**| The &#x60;thid&#x60;, shared between the inviter and the invitee, that uniquely identifies a connection flow. | [optional] 

### Return type

[**ConnectionsPage**](ConnectionsPage.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth), [jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

