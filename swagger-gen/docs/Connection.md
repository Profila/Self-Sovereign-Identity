# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The unique identifier of the connection. | 
**thid** | **str** | The unique identifier of the thread this connection record belongs to. The value will identical on both sides of the connection (inviter and invitee) | 
**label** | **str** | A human readable alias for the connection. | [optional] 
**goal_code** | **str** | A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message. | [optional] 
**goal** | **str** | A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message. | [optional] 
**my_did** | **str** | The DID representing me as the inviter or invitee in this specific connection. | [optional] 
**their_did** | **str** | The DID representing the other peer as the an inviter or invitee in this specific connection. | [optional] 
**role** | **str** | The role played by the Prism agent in the connection flow. | 
**state** | **str** | The current state of the connection protocol execution. | 
**invitation** | [**ConnectionInvitation**](ConnectionInvitation.md) |  | 
**created_at** | **datetime** | The date and time the connection record was created. | 
**updated_at** | **datetime** | The date and time the connection record was last updated. | [optional] 
**meta_retries** | **int** | The maximum background processing attempts remaining for this record | 
**_self** | **str** | The reference to the connection resource. | 
**kind** | **str** | The type of object returned. In this case a &#x60;Connection&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

