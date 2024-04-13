# Proof1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of cryptographic signature algorithm used to generate the proof. | 
**created** | **datetime** | The date and time at which the proof was created, in UTC format. This field is used to ensure that the proof was generated before or at the same time as the credential schema itself. | 
**verification_method** | **str** | The verification method used to generate the proof. This is usually a DID and key ID combination that can be used to look up the public key needed to verify the proof. | 
**proof_purpose** | **str** | The purpose of the proof (for example: &#x60;assertionMethod&#x60;). This indicates that the proof is being used to assert that the issuer really issued this credential schema instance. | 
**proof_value** | **str** | The cryptographic signature value that was generated using the private key associated with the verification method, and which can be used to verify the proof. | 
**jws** | **str** | The JSON Web Signature (JWS) that contains the proof information. | 
**domain** | **str** | It specifies the domain context within which the credential schema and proof are being used | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

