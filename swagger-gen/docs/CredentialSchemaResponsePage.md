# CredentialSchemaResponsePage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**list[CredentialSchemaResponse]**](CredentialSchemaResponse.md) | A sequence of CredentialSchemaResponse objects representing the list of credential schemas that the API response contains | [optional] 
**kind** | **str** | A string field indicating the type of the API response. In this case, it will always be set to &#x60;CredentialSchemaPage&#x60; | 
**_self** | **str** | A string field containing the URL of the current API endpoint | 
**page_of** | **str** | A string field indicating the type of resource that the contents field contains | 
**next** | **str** | An optional string field containing the URL of the next page of results. If the API response does not contain any more pages, this field should be set to None. | [optional] 
**previous** | **str** | An optional string field containing the URL of the previous page of results. If the API response is the first page of results, this field should be set to None. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

