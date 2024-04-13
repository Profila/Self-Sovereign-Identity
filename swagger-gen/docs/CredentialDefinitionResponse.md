# CredentialDefinitionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Globally unique id of the credential definition.It&#x27;s composed from the bytes of the string that contain the &#x60;author&#x60;, &#x60;name&#x60;, and &#x60;version&#x60; values.The string format looks like the resource identifier: &#x60;author&#x60;/&#x60;id&#x60;?version&#x3D;&#x60;version&#x60; | 
**id** | **str** | A locally unique identifier to address the credential definition. UUID is generated by the backend. | 
**long_id** | **str** | Resource id of the credential definition. Contains the &#x60;author&#x60;&#x27;s DID, &#x60;id&#x60; and &#x60;version&#x60; fields. | [optional] 
**name** | **str** | A human-readable name for the credential definition. A piece of Metadata. | 
**version** | **str** | Denotes the revision of a given Credential Definition. It should follow semantic version convention to describe the impact of the credential definition evolution. | 
**tag** | **str** | Token that allow to lookup and filter the credential definition records. | 
**description** | **str** | A human-readable description of the credential definition | 
**author** | **str** | DID of the identity which authored the credential definition. A piece of Metadata. | 
**authored** | **datetime** | [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) date on which the credential definition was created. A piece of Metadata. | 
**schema_id** | **str** | The unique identifier of the schema used for this credential definition. | 
**definition** | **object** | Definition object that represents the actual definition of the credential. | 
**key_correctness_proof** | **object** | A proof that validates the correctness of the key within the context of the credential definition. | 
**signature_type** | **str** | Signature type used in the CredentialDefinition. | 
**support_revocation** | **bool** | Boolean flag indicating whether revocation is supported for this CredentialDefinition. | 
**proof** | [**Proof**](Proof.md) |  | [optional] 
**kind** | **str** | A string that identifies the type of resource being returned in the response. | 
**_self** | **str** | The URL that uniquely identifies the resource being returned in the response. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
