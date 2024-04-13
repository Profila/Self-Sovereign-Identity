# VerificationPolicyResponsePage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_self** | **str** | The URL that uniquely identifies the resource being returned in the response. | 
**kind** | **str** | A string that identifies the type of resource being returned in the response. | 
**page_of** | **str** | A string field indicating the type of resource that the contents field contains | 
**next** | **str** | An optional string field containing the URL of the next page of results. If the API response does not contain any more pages, this field should be set to None. | [optional] 
**previous** | **str** | An optional string field containing the URL of the previous page of results. If the API response is the first page of results, this field should be set to None. | [optional] 
**contents** | [**list[VerificationPolicyResponse]**](VerificationPolicyResponse.md) | A sequence of VerificationPolicyResponse objects representing the list of verification policies that the paginated response contains | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

