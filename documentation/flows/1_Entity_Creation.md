# Entity Creation

The API can create three types of entities:
1. **User/Person**
    - An entity capable of receiving Verifiable Credentials (VCs) and sharing the data in those VCs with brands via presentations.
2. **Issuer**
    - An entity that can create schemas (templates with specific data fields to store user information) and issue VCs to users based on those schemas.
3. **Brand**
    - An entity that can request data from users via presentation requests.

## Create Entity Flow

To create an entity, follow these steps:

1. Send a POST request to the `/create-entity/{entity_type}` endpoint.
2. Replace `{entity_type}` with "user", "issuer", or "brand".
3. Example of a request body:
    ```json
    {
      "name": "Test_User"
    }
    ```
4. Upon successful creation, the API will return a response with details of the newly created entity. A wallet and an authorization API key are also generated for the entity.

### Example Request

```bash
curl -X 'POST' \
  'http://129.151.179.222:8000/create-entity/user' \
  -H 'accept: application/json' \
  -H 'x-admin-api-key: my-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "Elmer_Test"
    }'
```

### Example Response

```json
{
  "userId": "180ebf7b-d49f-4910-92b8-3aaea4ee5a3e",
  "walletId": "ffcec57e-4821-4565-9479-5d91cd25b522",
  "did": "did:prism:027dbb710f7c3f3301b0e387a40d2e13a8c46edbba63e4fca190987f1182b2ca:CnsKeRI6CgZhdXRoLTEQBEouCglzZWNwMjU2azESIQLhK1MWHE_qDN70ZVGz-d5oglBctpZaekrTiUeNYPcV0BI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiED8PxAsrLfOJSpNxF1lWBMa6DkYoANOvB-J6uQXs4Qp_Y",
  "entityApiKey": "user.wgTLw6hlclMBb7aNLFIQ0xw3fCxvmPR1"
}
```

Note that the API key will start with "user.", "issuer.", or "brand." depending on the type of entity created.

## View Entity
To verify that an entity has been created, use the `/view-entity/{id}` endpoint where `{id}` is the `entityId` returned in the previous step.

