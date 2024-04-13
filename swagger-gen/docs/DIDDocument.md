# DIDDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **list[str]** |  | [optional] 
**id** | **str** | [DID subject](https://www.w3.org/TR/did-core/#did-subject). The value must match the DID that was given to the resolver. | 
**controller** | **str** | [DID controller](https://www.w3.org/TR/did-core/#did-controller) | [optional] 
**verification_method** | [**list[VerificationMethod]**](VerificationMethod.md) |  | [optional] 
**authentication** | **list[str]** |  | [optional] 
**assertion_method** | **list[str]** |  | [optional] 
**key_agreement** | **list[str]** |  | [optional] 
**capability_invocation** | **list[str]** |  | [optional] 
**capability_delegation** | **list[str]** |  | [optional] 
**service** | [**list[Service]**](Service.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

