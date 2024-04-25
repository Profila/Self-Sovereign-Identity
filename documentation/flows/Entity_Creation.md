# Entity Creation

The api can create three types of entities namely
1. User/Person
    - An entity that is able to receive VCs and share the data in those VCs with brands via presentations.
2. Issuer
    - An entity that can create schemas (Templates with certain data fields to store user information) and issue VCs to users that are based on those schemas.
3. Brand
    - An entity that can request data from users via presentation requests.

## User/Person

To create a user/person entity, follow these steps:

1. Send a POST request to the `/create-entity/{entity_type}` endpoint.
2. {entity_type} should be "user".
3. Upon successful creation, the API will return a response with the newly created user/person entity.

Example request:

curl -X 'POST' \
  'http://129.151.179.222:8000/create-entity/user' \
  -H 'accept: application/json' \
  -H 'x-admin-api-key: my-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Elmer_Test"
}'