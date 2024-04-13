# IssueCredentialRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** |  The unique identifier of the issue credential record. This identifier is internal to the agent and not shared between issuer and holder.  | 
**thid** | **str** |  The unique identifier of the &#x27;thread&#x27; identifying the specific issuance flow execution as a whole. This same unique &#x27;thid&#x27; value is included in every message exchanged during the flow execution. It is shared between the issuer and the holder agents and its value identical on both sides.  | 
**credential_format** | **str** | The credential format for this offer. | 
**subject_id** | **str** |  The short-form subject Prism DID to which the JWT verifiable credential will be or has been issued. This parameter only applies if the offer is of type &#x27;JWT&#x27; and will only exist in the cloud agent of the holder (it will be empty on the issuer side).  | [optional] 
**validity_period** | **float** |  The validity period in seconds of the verifiable credential that will be issued. This parameter will only exist in the cloud agent of the issuer (it will be empty on the holder side).  | [optional] 
**claims** | **object** |  The set of claims included in the issued credential.  | 
**automatic_issuance** | **bool** |  Specifies whether or not the credential is automatically generated and issued when receiving the &#x60;CredentialRequest&#x60; from the holder. If set to &#x60;false&#x60;, a manual approval by the issuer via another API call will be required for the VC to be issued. This parameter will only exist in the cloud agent of the issuer (it will be empty on the holder side).  | [optional] 
**created_at** | **datetime** | The date and time when the issue credential record was created. | 
**updated_at** | **datetime** | The date and time when the issue credential record was last updated. | [optional] 
**role** | **str** | The role played by the agent in the credential issuance flow. | 
**protocol_state** | **str** | The current state of the issue credential protocol execution. | 
**credential** | **str** | The base64-encoded credential that was issued by the issuer agent, in &#x27;JWT&#x27; or &#x27;AnonCreds&#x27; format depending on the offer type. | [optional] 
**issuing_did** | **str** |  The short-form issuer Prism DID by which the JWT verifiable credential will be or has been issued. Note that this parameter only applies when the offer is type &#x27;JWT&#x27;.  | [optional] 
**meta_retries** | **int** | The maximum background processing attempts remaining for this record. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

