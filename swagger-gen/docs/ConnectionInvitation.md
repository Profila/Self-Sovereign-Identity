# ConnectionInvitation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the invitation. It should be used as parent thread ID (pthid) for the Connection Request message that follows. | 
**type** | **str** | The DIDComm Message Type URI (MTURI) the invitation message complies with. | 
**_from** | **str** | The DID representing the sender to be used by recipients for future interactions. | 
**invitation_url** | **str** | The invitation message encoded as a URL. This URL follows the Out of [Band 2.0 protocol](https://identity.foundation/didcomm-messaging/spec/v2.0/#out-of-band-messages) and can be used to generate a QR code for example. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

