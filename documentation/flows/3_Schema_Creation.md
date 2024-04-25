# Schema Creation

In order for an issuer to issue a VC to a user a schema will be needed first (A schema is also created by the issuer in this implementation).

## Create Schema Flow

To create a schema, follow these steps:

1. Send a POST request to the issuer `/create-schema/` endpoint.
2. Provide the issuer did and issuer api key. The issuer did should be in short form. 
    - Short form example:
        - did:prism:dbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e
    - Long form example:
        - did:prism:dbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e:CnsKeRI6CgZhdXRoLTEQAkouCglzZWNwMjU2azESIQM1PA7297szag90-q_zZuRerLL6aT0iGKdG6ailz_5hQhI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiEDZv6-29wcgxUA6UGv6X3G8IXJ-a9BbJXs1R3NoGI-jT4
3. Fill out the request body (See example request). 
4. Upon successful creation, the API will return a response with the newly created schema information.

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/create-schema/?issuer_did=did%3Aprism%3Adbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e' \
  -H 'accept: application/json' \
  -H 'issuer-api-key: issuer.ulzZEloZSahxaUvmMQcct6znLizKuaOB' \
  -H 'Content-Type: application/json' \
  -d '{
  "schemaName": "Doc_Test_Profile_2",
  "schemaVersion": "1.0.0",
  "schemaDescription": "This is a doc test schema",
  "schemaId": "https://profila.com/profila-profile-1.0.0",
  "schemaTags": [
    "test",
    "docs"
  ],
  "attributes": [
    {
      "name": "email",
      "dataType": "string"
    },
    {
      "name": "firstname",
      "dataType": "string"
    },
    {
      "name": "surname",
      "dataType": "string"
    },
    {
      "name": "age",
      "dataType": "string"
    }
  ]
}'
```
Example response:

```
{
  "guid": "cb26f2d5-3e0c-343f-8502-0812ab519c47",
  "id": "6f8dfe0d-a529-487b-93d1-25b30a50ec98",
  "long_id": "did:prism:dbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e/6f8dfe0d-a529-487b-93d1-25b30a50ec98?version=1.0.0",
  "name": "Doc_Test_Profile_2",
  "version": "1.0.0",
  "tags": [
    "test",
    "docs"
  ],
  "description": "This is a doc test schema",
  "type": "https://w3c-ccg.github.io/vc-json-schemas/schema/2.0/schema.json",
  "schema": {
    "$id": "https://profila.com/profila-profile-1.0.0",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "email": {
        "type": "string"
      },
      "firstname": {
        "type": "string"
      },
      "surname": {
        "type": "string"
      },
      "age": {
        "type": "string"
      }
    },
    "required": [
      "email",
      "firstname",
      "surname",
      "age"
    ],
    "additionalProperties": false
  },
  "author": "did:prism:dbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e",
  "authored": "2024-04-25T13:36:03.835628Z",
  "proof": null,
  "kind": "CredentialSchema"
}
```

## View Schema
To verify that a schema was created, use the `/view-schema/{id}` endpoint where `{id}` is the `guid` returned in the previous step. 
