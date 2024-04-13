# CreateIssueCredentialRecordRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validity_period** | **float** | The validity period in seconds of the verifiable credential that will be issued. | [optional] 
**schema_id** | **str** |  The URL pointing to the JSON schema that will be used for this offer (should be &#x27;http&#x27; or &#x27;https&#x27;). When dereferenced, the returned content should be a JSON schema compliant with the &#x27;[Draft 2020-12](https://json-schema.org/draft/2020-12/release-notes)&#x27; version of the specification. Note that this parameter only applies when the offer is of type &#x27;JWT&#x27;.  | [optional] 
**credential_definition_id** | **str** |  The unique identifier (UUID) of the credential definition that will be used for this offer. It should be the identifier of a credential definition that exists in the issuer agent&#x27;s database. Note that this parameter only applies when the offer is of type &#x27;AnonCreds&#x27;.  | [optional] 
**credential_format** | **str** | The credential format for this offer (defaults to &#x27;JWT&#x27;) | [optional] 
**claims** | **object** |  The set of claims that will be included in the issued credential. The JSON object should comply with the schema applicable for this offer (i.e. &#x27;schemaId&#x27; or &#x27;credentialDefinitionId&#x27;).  | 
**automatic_issuance** | **bool** |  Specifies whether or not the credential should be automatically generated and issued when receiving the &#x60;CredentialRequest&#x60; from the holder. If set to &#x60;false&#x60;, a manual approval by the issuer via another API call will be required for the VC to be issued.  | [optional] 
**issuing_did** | **str** |  The short-form issuer Prism DID by which the JWT verifiable credential will be issued. Note that this parameter only applies when the offer is type &#x27;JWT&#x27;.  | [optional] 
**connection_id** | **str** |  The unique identifier of a DIDComm connection that already exists between the this issuer agent and the holder cloud or edeg agent. It should be the identifier of a connection that exists in the issuer agent&#x27;s database. This connection will be used to execute the issue credential protocol.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

