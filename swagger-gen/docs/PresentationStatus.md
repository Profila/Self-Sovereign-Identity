# PresentationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**presentation_id** | **str** | The unique identifier of the presentation record. | 
**thid** | **str** | The unique identifier of the thread this presentation record belongs to. The value will identical on both sides of the presentation flow (verifier and prover) | 
**role** | **str** | The role played by the Prism agent in the proof presentation flow. | 
**status** | **str** | The current state of the proof presentation record. | 
**proofs** | [**list[ProofRequestAux]**](ProofRequestAux.md) | The type of proofs requested in the context of this proof presentation request (e.g., VC schema, trusted issuers, etc.) | [optional] 
**data** | **list[str]** | The list of proofs presented by the prover to the verifier. | [optional] 
**connection_id** | **str** | The unique identifier of an established connection between the verifier and the prover. | [optional] 
**meta_retries** | **int** | The maximum background processing attempts remaining for this record | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

