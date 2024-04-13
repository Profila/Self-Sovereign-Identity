# RequestPresentationInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The unique identifier of an established connection between the verifier and the prover. | 
**options** | [**Options**](Options.md) |  | [optional] 
**proofs** | [**list[ProofRequestAux]**](ProofRequestAux.md) | The type of proofs requested in the context of this proof presentation request (e.g., VC schema, trusted issuers, etc.) | [optional] 
**anoncred_presentation_request** | [**AnoncredPresentationRequestV1**](AnoncredPresentationRequestV1.md) |  | [optional] 
**credential_format** | **str** | The credential format (default to &#x27;JWT&#x27;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

