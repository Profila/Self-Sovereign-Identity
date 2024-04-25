# Entity Creation

The api can create three types of entities namely
1. User/Person
    - An entity that is able to receive VCs (Verifiable Credentials) and share the data in those VCs with brands via presentations.
2. Issuer
    - An entity that can create schemas (Templates with certain data fields to store user information) and issue VCs to users that are based on those schemas.
3. Brand
    - An entity that can request data from users via presentation requests.

## Create Entity Flow

To create a entity, follow these steps:

1. Send a POST request to the `/create-entity/{entity_type}` endpoint.
2. {entity_type} should be "user", "issuer" or "brand".
3. Request body example:
    - {
        "name": "Test_User"
      }
4. Upon successful creation, the API will return a response with the newly created user/person entity. A wallet and authorization api key is also created for the entity.

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/create-entity/user' \
  -H 'accept: application/json' \
  -H 'x-admin-api-key: my-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Elmer_Test"
}'
```
Example response:

```
{
  "userId": "180ebf7b-d49f-4910-92b8-3aaea4ee5a3e",
  "walletId": "ffcec57e-4821-4565-9479-5d91cd25b522",
  "did": "did:prism:027dbb710f7c3f3301b0e387a40d2e13a8c46edbba63e4fca190987f1182b2ca:CnsKeRI6CgZhdXRoLTEQBEouCglzZWNwMjU2azESIQLhK1MWHE_qDN70ZVGz-d5oglBctpZaekrTiUeNYPcV0BI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiED8PxAsrLfOJSpNxF1lWBMa6DkYoANOvB-J6uQXs4Qp_Y",
  "entityApiKey": "user.wgTLw6hlclMBb7aNLFIQ0xw3fCxvmPR1"
}
```

## View Entity
To verify that an entity is created use the `/view-entity/{id}` endpoint where `{id}` is the `entityId` returned in the previous step.