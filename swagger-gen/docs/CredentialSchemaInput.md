# CredentialSchemaInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for the credential schema. A piece of Metadata. | 
**version** | **str** | Denotes the revision of a given Credential Schema. It should follow semantic version convention to describe the impact of the schema evolution. | 
**description** | **str** | A human-readable description of the credential schema | [optional] 
**type** | **str** | This field resolves to a JSON schema with details about the schema metadata that applies to the schema. A piece of Metadata. | 
**schema** | **object** | Valid JSON Schema where the Credential Schema data fields are defined. A piece of Metadata | 
**tags** | **list[str]** | Tokens that allow to lookup and filter the credential schema records. | [optional] 
**author** | **str** | DID of the identity which authored the credential schema. A piece of Metadata. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

