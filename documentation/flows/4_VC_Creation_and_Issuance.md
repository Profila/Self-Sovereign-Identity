# Verifiable Credential Issuance

An issuer can issue a credential based on a published schema to a user if they have an established connection between them.

## Issuer VC Issuance Flow

To issue a VC, follow these steps:

1. Send a POST request to the issuer `/offer-credential/` endpoint.
2. Provide the schema id and issuer api key. The schema id is its `guid`.
3. Fill out the request body to make claims about a user/person (See example request). Provide the did of the issuer and the connection id of the connection between the issuer and relevant user.
4. Upon success, the API will return a response with the newly created credential offer information.

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/offer-credential/?schema_id=cb26f2d5-3e0c-343f-8502-0812ab519c47' \
  -H 'accept: application/json' \
  -H 'issuer-api-key: issuer.ulzZEloZSahxaUvmMQcct6znLizKuaOB' \
  -H 'Content-Type: application/json' \
  -d '{
  "issuerDid": "did:prism:dbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e",
  "connectionId": "3fb9d7fc-6519-4883-9fbe-62bd693ed56e",
  "attrClaims": [
    {
      "name": "email",
      "value": "alice@gmail.com"
    },
    {
      "name": "firstname",
      "value": "Alice"
    },
    {
      "name": "surname",
      "value": "Doe"
    },
    {
      "name": "age",
      "value": "30"
    }
  ]
}'
```
Example response:

```
{
  "record_id": "5befe547-ee2f-4e49-b096-6526cd090c61",
  "thid": "a39cf375-34ef-4345-8103-61c1a06a93fd",
  "credential_format": "JWT",
  "subject_id": null,
  "validity_period": 86400,
  "claims": {
    "email": "alice@gmail.com",
    "firstname": "Alice",
    "surname": "Doe",
    "age": "30"
  },
  "automatic_issuance": true,
  "created_at": "2024-04-25T13:56:39.691653Z",
  "updated_at": "2024-04-25T13:56:42.229682Z",
  "role": "Issuer",
  "protocol_state": "OfferSent",
  "credential": null,
  "issuing_did": null,
  "meta_retries": 5
}
```

## User Views and Accepts New VC Offer

To view VC offers execute the following steps:

1. Send a GET request to the **USERs** `/list-credential-offers/` to check for a new offer in the `OfferReceived` state. 
    - Note that the id is different than it was in the response when the offer was created by the issuer. Each entity tracks objects with their own ids.
2. Provide the user api key. Note that in the given example only one offer is present but there could be more than one.

Example request:

```
curl -X 'GET' \
  'http://129.151.179.222:8000/list-credential-offers/' \
  -H 'accept: application/json' \
  -H 'user-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo'
```
Example response:

```
[
  {
    "record_id": "30bbfea7-7d0f-474a-89af-14f6e7cebe60",
    "thid": "a39cf375-34ef-4345-8103-61c1a06a93fd",
    "credential_format": "JWT",
    "subject_id": null,
    "validity_period": null,
    "claims": {
      "email": "alice@gmail.com",
      "firstname": "Alice",
      "surname": "Doe",
      "age": "30"
    },
    "automatic_issuance": null,
    "created_at": "2024-04-25T13:56:40.200145Z",
    "updated_at": null,
    "role": "Holder",
    "protocol_state": "OfferReceived",
    "credential": null,
    "issuing_did": null,
    "meta_retries": 5
  }
]
```

3. User identifies which offer to accept from the above list and responds with a POST request to the `/accept-credential-offer/{id}`. The `id` is the `record_id` returned in the previous step.
4. Provide the user api key. The subject id is the short form did of the user. 

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/accept-credential-offer/30bbfea7-7d0f-474a-89af-14f6e7cebe60?subjectId=did%3Aprism%3A7950134acdce3949b6751cf7b6770f151326191ce62274bb44be0d3867d249c8' \
  -H 'accept: application/json' \
  -H 'user-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo' \
  -d ''
```
Example response:

```
{
  "record_id": "30bbfea7-7d0f-474a-89af-14f6e7cebe60",
  "thid": "a39cf375-34ef-4345-8103-61c1a06a93fd",
  "credential_format": "JWT",
  "subject_id": "did:prism:7950134acdce3949b6751cf7b6770f151326191ce62274bb44be0d3867d249c8",
  "validity_period": null,
  "claims": {
    "email": "alice@gmail.com",
    "firstname": "Alice",
    "surname": "Doe",
    "age": "30"
  },
  "automatic_issuance": null,
  "created_at": "2024-04-25T13:56:40.200145Z",
  "updated_at": "2024-04-25T14:16:04.417249Z",
  "role": "Holder",
  "protocol_state": "RequestPending",
  "credential": null,
  "issuing_did": null,
  "meta_retries": 5
}
```

5. Check if VC was received by making a GET request to the `/view-credential/{id}` endpoint where the `id` is the `record_id` of the VC.
6. Provide the user api key.

Example request:

```
curl -X 'GET' \
  'http://129.151.179.222:8000/view-credential/30bbfea7-7d0f-474a-89af-14f6e7cebe60' \
  -H 'accept: application/json' \
  -H 'user-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo'
```
Example response:

```
{
  "record_id": "30bbfea7-7d0f-474a-89af-14f6e7cebe60",
  "thid": "a39cf375-34ef-4345-8103-61c1a06a93fd",
  "credential_format": "JWT",
  "subject_id": "did:prism:7950134acdce3949b6751cf7b6770f151326191ce62274bb44be0d3867d249c8",
  "validity_period": null,
  "claims": {
    "email": "alice@gmail.com",
    "firstname": "Alice",
    "surname": "Doe",
    "age": "30"
  },
  "automatic_issuance": null,
  "created_at": "2024-04-25T13:56:40.200145Z",
  "updated_at": "2024-04-25T14:16:16.761225Z",
  "role": "Holder",
  "protocol_state": "CredentialReceived",
  "credential": "ZXlKaGJHY2lPaUpGVXpJMU5rc2lmUS5leUpwYzNNaU9pSmthV1E2Y0hKcGMyMDZaR0prTURRNU9XTmhPVEUzWTJSa1pHVXlNV0l3WVRCalptRTFOelptT0RNeU9EZGlNVFUyWkRsak9HRm1NR1JsWldOa1pqRXpPV0k1WXpJd09UQTBaVHBEYm5OTFpWSkpOa05uV21oa1dGSnZURlJGVVVGcmIzVkRaMng2V2xkT2QwMXFWVEpoZWtWVFNWRk5NVkJCTnpJNU4zTjZZV2M1TUMxeFgzcGFkVkpsY2t4TU5tRlVNR2xIUzJSSE5tRnBiSHBmTldoUmFFazNRMmRrZEZsWVRqQmFXRWwzUlVGR1MweG5iMHBqTWxacVkwUkpNVTV0YzNoRmFVVkVXblkyTFRJNWQyTm5lRlZCTmxWSGRqWllNMGM0U1ZoS0xXRTVRbUpLV0hNeFVqTk9iMGRKTFdwVU5DSXNJbk4xWWlJNkltUnBaRHB3Y21semJUbzNPVFV3TVRNMFlXTmtZMlV6T1RRNVlqWTNOVEZqWmpkaU5qYzNNR1l4TlRFek1qWXhPVEZqWlRZeU1qYzBZbUkwTkdKbE1HUXpPRFkzWkRJME9XTTRPa051YzB0bFVrazJRMmRhYUdSWVVtOU1WRVZSUWtWdmRVTm5iSHBhVjA1M1RXcFZNbUY2UlZOSlVWQmlaWEJmZGtob2FrdHVWVlZMZDJ0R1FUTlRZMWxuTTBSRFQwdGpWMk5hWVhKeFFVMDRRV2wxTFY5NFNUZERaMlIwV1ZoT01GcFlTWGRGUVVaTFRHZHZTbU15Vm1walJFa3hUbTF6ZUVWcFJVUjBVa2hUYkZjMFEydGlVakp3VkVVME9WQmZWbkpMTTNWTFltRkZRM3BZZUU5SWNEbDRZbnAzVFVNNElpd2libUptSWpveE56RTBNRFUwTlRjMExDSmxlSEFpT2pFM01UUXhOREE1TnpRc0luWmpJanA3SW1OeVpXUmxiblJwWVd4VFkyaGxiV0VpT25zaWFXUWlPaUpvZEhSd09sd3ZYQzh4TWprdU1UVXhMakUzT1M0eU1qSTZPREE0TUZ3dmNISnBjMjB0WVdkbGJuUmNMM05qYUdWdFlTMXlaV2RwYzNSeWVWd3ZjMk5vWlcxaGMxd3ZZMkl5Tm1ZeVpEVXRNMlV3WXkwek5ETm1MVGcxTURJdE1EZ3hNbUZpTlRFNVl6UTNJaXdpZEhsd1pTSTZJa055WldSbGJuUnBZV3hUWTJobGJXRXlNREl5SW4wc0ltTnlaV1JsYm5ScFlXeFRkV0pxWldOMElqcDdJbVpwY25OMGJtRnRaU0k2SWtGc2FXTmxJaXdpYzNWeWJtRnRaU0k2SWtSdlpTSXNJbWxrSWpvaVpHbGtPbkJ5YVhOdE9qYzVOVEF4TXpSaFkyUmpaVE01TkRsaU5qYzFNV05tTjJJMk56Y3daakUxTVRNeU5qRTVNV05sTmpJeU56UmlZalEwWW1Vd1pETTROamRrTWpRNVl6ZzZRMjV6UzJWU1NUWkRaMXBvWkZoU2IweFVSVkZDUlc5MVEyZHNlbHBYVG5kTmFsVXlZWHBGVTBsUlVHSmxjRjkyU0docVMyNVZWVXQzYTBaQk0xTmpXV2N6UkVOUFMyTlhZMXBoY25GQlRUaEJhWFV0WDNoSk4wTm5aSFJaV0U0d1dsaEpkMFZCUmt0TVoyOUtZekpXYW1ORVNURk9iWE40UldsRlJIUlNTRk5zVnpSRGEySlNNbkJVUlRRNVVGOVdja3N6ZFV0aVlVVkRlbGg0VDBod09YaGllbmROUXpnaUxDSmxiV0ZwYkNJNkltRnNhV05sUUdkdFlXbHNMbU52YlNJc0ltRm5aU0k2SWpNd0luMHNJblI1Y0dVaU9sc2lWbVZ5YVdacFlXSnNaVU55WldSbGJuUnBZV3dpWFN3aVFHTnZiblJsZUhRaU9sc2lhSFIwY0hNNlhDOWNMM2QzZHk1M015NXZjbWRjTHpJd01UaGNMMk55WldSbGJuUnBZV3h6WEM5Mk1TSmRmWDAubmpWZEZGa0gzUEstYWZ2Mi16NDAzOG9sYTlHX0d2Y3VrMzBtNzI5LXVFZy1xN3hQVlJqRjV5TU1JekVWSkhfZmxyZjZSaEFtZkp4anNIM2pBRnZLeEE=",
  "issuing_did": null,
  "meta_retries": 5
}
```

7. Ensure that it is in the `CredentialReceived` state.