# DIDDocumentMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivated** | **bool** | If a DID has been deactivated, DID document metadata MUST include this property with the boolean value true. If a DID has not been deactivated, this property is OPTIONAL, but if included, MUST have the boolean value false. | [optional] 
**canonical_id** | **str** |  A DID in canonical form. If a DID is in long form and has been published, DID document metadata MUST contain a &#x60;canonicalId&#x60;&#x60; property with the short form DID as its value. If a DID in short form or has not been published, DID document metadata MUST NOT contain a &#x60;canonicalId&#x60; property.  | [optional] 
**version_id** | **str** |  DID document metadata MUST contain a versionId property with the hash of the AtalaOperation contained in the latest valid SignedAtalaOperation that created the DID or changed the DID&#x27;s internal state.  | [optional] 
**created** | **str** | The timestamp of the Cardano block that contained the first valid SignedAtalaOperation with a CreateDIDOperation that created the DID. | [optional] 
**updated** | **str** | The timestamp of the Cardano block that contained the latest valid SignedAtalaOperation that changed the DID&#x27;s internal state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

