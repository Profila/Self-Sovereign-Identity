# CredentialDefinitionInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for the credential definition. A piece of Metadata. | 
**description** | **str** | A human-readable description of the credential definition | [optional] 
**version** | **str** | Denotes the revision of a given Credential Definition. It should follow semantic version convention to describe the impact of the credential definition evolution. | 
**tag** | **str** | Token that allow to lookup and filter the credential definition records. | 
**author** | **str** | DID of the identity which authored the credential definition. A piece of Metadata. | 
**schema_id** | **str** | The unique identifier of the schema used for this credential definition. | 
**signature_type** | **str** | Signature type used in the CredentialDefinition. | 
**support_revocation** | **bool** | Boolean flag indicating whether revocation is supported for this CredentialDefinition. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

