# StatusListCredential

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **list[str]** | List of JSON-LD contexts | [optional] 
**type** | **list[str]** | List of credential types | [optional] 
**issuer** | **str** | DID of the issuer of status list credential | 
**id** | **str** | Unique identifier of status list credential | 
**issuance_date** | **datetime** | Issuance timestamp of status list credential | 
**credential_subject** | [**CredentialSubject**](CredentialSubject.md) |  | 
**proof** | **object** | Embedded proof to verify data integrity of status list credential, includes \&quot;type\&quot; property which defines an algorithm to be used for proof verification | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

