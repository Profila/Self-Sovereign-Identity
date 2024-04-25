# Verifiable Credential Presentation

A brand can request a presentation from a user if they have an established connection between them.

## Brand Presentation Request Flow

To make a presentation request, follow these steps:

1. Send a POST request to the brand `/create-presentation-request/` endpoint.
2. Provide the connection id and brand API key. The trusted issuer did is its short form did of the issuer that issued the VC to the user.
3. Upon success, the API will return a response with the newly created presentation request information.

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/create-presentation-request/?connection_id=39deadba-16f1-4fff-85df-2e446265b122&trusted_issuer_did=did%3Aprism%3Adbd0499ca917cddde21b0a0cfa576f83287b156d9c8af0deecdf139b9c20904e' \
  -H 'accept: application/json' \
  -H 'brand-api-key: brand.VvI2TlftM0M4pZIDWRaLGpOLFMhqgbli' \
  -d ''
```
Example response:

```
{
  "presentation_id": "738a994b-30c5-428f-a522-d2c1ca0b9be5",
  "thid": "6b8efe34-a5b8-44fb-958d-53f6c93c6af3",
  "role": "Verifier",
  "status": "RequestPending",
  "proofs": [],
  "data": [],
  "connection_id": "39deadba-16f1-4fff-85df-2e446265b122",
  "meta_retries": 5
}
```

## User Views and Accepts New Presentation Request

To view presentation requests execute the following steps:

1. Send a GET request to the **USER** `/list-presentation-requests/` to check for a new request in the `RequestReceived` state. 
    - Note that the id is different than it was in the response when the request was created by the brand. Each entity tracks objects with their own ids.
2. Provide the user api key. Note that in the given example only one request is present but there could be more than one.

Example request:

```
curl -X 'GET' \
  'http://129.151.179.222:8000/list-presentation-requests/' \
  -H 'accept: application/json' \
  -H 'requestor-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo'
```
Example response:

```
{
  "contents": [
    {
      "presentation_id": "d393ac22-2cfc-47d9-a875-7caba5807936",
      "thid": "6b8efe34-a5b8-44fb-958d-53f6c93c6af3",
      "role": "Prover",
      "status": "RequestReceived",
      "proofs": [],
      "data": [],
      "connection_id": null,
      "meta_retries": 5
    }
  ],
  "kind": "Collection",
  "page_of": "1",
  "next": null,
  "previous": null
}
```

3. User identifies which request to respond to from the above list and responds with a POST request to the `/present-credential/{id}`. The `id` is the `presentation_id` returned in the previous step.
4. Provide the user api key. The vc_record_id is the record id of the VC to use for the presentation. 

Example request:

```
curl -X 'POST' \
  'http://129.151.179.222:8000/present-credential/d393ac22-2cfc-47d9-a875-7caba5807936?vc_record_id=30bbfea7-7d0f-474a-89af-14f6e7cebe60' \
  -H 'accept: application/json' \
  -H 'user-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo' \
  -d ''
```
Example response:

```
{
  "presentation_id": "d393ac22-2cfc-47d9-a875-7caba5807936",
  "thid": "6b8efe34-a5b8-44fb-958d-53f6c93c6af3",
  "role": "Prover",
  "status": "PresentationPending",
  "proofs": [],
  "data": [],
  "connection_id": null,
  "meta_retries": 5
}
```

5. Check if presentation was received by the **brand** making a GET request to the **brands** `/view-presentation-request/{id}` endpoint where the `id` is the `presentation_id`.
6. Provide the brand api key.

Example request:

```
curl -X 'GET' \
  'http://129.151.179.222:8000/view-presentation-request/738a994b-30c5-428f-a522-d2c1ca0b9be5' \
  -H 'accept: application/json' \
  -H 'requestor-api-key: brand.VvI2TlftM0M4pZIDWRaLGpOLFMhqgbli'
```
Example response:

```
{
  "presentation_id": "738a994b-30c5-428f-a522-d2c1ca0b9be5",
  "thid": "6b8efe34-a5b8-44fb-958d-53f6c93c6af3",
  "role": "Verifier",
  "status": "PresentationVerified",
  "proofs": [],
  "data": [
    "eyJhbGciOiJFUzI1NksifQ.eyJpc3MiOiJkaWQ6cHJpc206Nzk1MDEzNGFjZGNlMzk0OWI2NzUxY2Y3YjY3NzBmMTUxMzI2MTkxY2U2MjI3NGJiNDRiZTBkMzg2N2QyNDljODpDbnNLZVJJNkNnWmhkWFJvTFRFUUJFb3VDZ2x6WldOd01qVTJhekVTSVFQYmVwX3ZIaGpLblVVS3drRkEzU2NZZzNEQ09LY1djWmFycUFNOEFpdS1feEk3Q2dkdFlYTjBaWEl3RUFGS0xnb0pjMlZqY0RJMU5tc3hFaUVEdFJIU2xXNENrYlIycFRFNDlQX1ZySzN1S2JhRUN6WHhPSHA5eGJ6d01DOCIsImF1ZCI6Imh0dHBzOlwvXC9wcm9maWxhLmNvbSIsInZwIjp7InR5cGUiOlsiVmVyaWZpYWJsZVByZXNlbnRhdGlvbiJdLCJAY29udGV4dCI6WyJodHRwczpcL1wvd3d3LnczLm9yZ1wvMjAxOFwvcHJlc2VudGF0aW9uc1wvdjEiXSwidmVyaWZpYWJsZUNyZWRlbnRpYWwiOlsiZXlKaGJHY2lPaUpGVXpJMU5rc2lmUS5leUpwYzNNaU9pSmthV1E2Y0hKcGMyMDZaR0prTURRNU9XTmhPVEUzWTJSa1pHVXlNV0l3WVRCalptRTFOelptT0RNeU9EZGlNVFUyWkRsak9HRm1NR1JsWldOa1pqRXpPV0k1WXpJd09UQTBaVHBEYm5OTFpWSkpOa05uV21oa1dGSnZURlJGVVVGcmIzVkRaMng2V2xkT2QwMXFWVEpoZWtWVFNWRk5NVkJCTnpJNU4zTjZZV2M1TUMxeFgzcGFkVkpsY2t4TU5tRlVNR2xIUzJSSE5tRnBiSHBmTldoUmFFazNRMmRrZEZsWVRqQmFXRWwzUlVGR1MweG5iMHBqTWxacVkwUkpNVTV0YzNoRmFVVkVXblkyTFRJNWQyTm5lRlZCTmxWSGRqWllNMGM0U1ZoS0xXRTVRbUpLV0hNeFVqTk9iMGRKTFdwVU5DSXNJbk4xWWlJNkltUnBaRHB3Y21semJUbzNPVFV3TVRNMFlXTmtZMlV6T1RRNVlqWTNOVEZqWmpkaU5qYzNNR1l4TlRFek1qWXhPVEZqWlRZeU1qYzBZbUkwTkdKbE1HUXpPRFkzWkRJME9XTTRPa051YzB0bFVrazJRMmRhYUdSWVVtOU1WRVZSUWtWdmRVTm5iSHBhVjA1M1RXcFZNbUY2UlZOSlVWQmlaWEJmZGtob2FrdHVWVlZMZDJ0R1FUTlRZMWxuTTBSRFQwdGpWMk5hWVhKeFFVMDRRV2wxTFY5NFNUZERaMlIwV1ZoT01GcFlTWGRGUVVaTFRHZHZTbU15Vm1walJFa3hUbTF6ZUVWcFJVUjBVa2hUYkZjMFEydGlVakp3VkVVME9WQmZWbkpMTTNWTFltRkZRM3BZZUU5SWNEbDRZbnAzVFVNNElpd2libUptSWpveE56RTBNRFUwTlRjMExDSmxlSEFpT2pFM01UUXhOREE1TnpRc0luWmpJanA3SW1OeVpXUmxiblJwWVd4VFkyaGxiV0VpT25zaWFXUWlPaUpvZEhSd09sd3ZYQzh4TWprdU1UVXhMakUzT1M0eU1qSTZPREE0TUZ3dmNISnBjMjB0WVdkbGJuUmNMM05qYUdWdFlTMXlaV2RwYzNSeWVWd3ZjMk5vWlcxaGMxd3ZZMkl5Tm1ZeVpEVXRNMlV3WXkwek5ETm1MVGcxTURJdE1EZ3hNbUZpTlRFNVl6UTNJaXdpZEhsd1pTSTZJa055WldSbGJuUnBZV3hUWTJobGJXRXlNREl5SW4wc0ltTnlaV1JsYm5ScFlXeFRkV0pxWldOMElqcDdJbVpwY25OMGJtRnRaU0k2SWtGc2FXTmxJaXdpYzNWeWJtRnRaU0k2SWtSdlpTSXNJbWxrSWpvaVpHbGtPbkJ5YVhOdE9qYzVOVEF4TXpSaFkyUmpaVE01TkRsaU5qYzFNV05tTjJJMk56Y3daakUxTVRNeU5qRTVNV05sTmpJeU56UmlZalEwWW1Vd1pETTROamRrTWpRNVl6ZzZRMjV6UzJWU1NUWkRaMXBvWkZoU2IweFVSVkZDUlc5MVEyZHNlbHBYVG5kTmFsVXlZWHBGVTBsUlVHSmxjRjkyU0docVMyNVZWVXQzYTBaQk0xTmpXV2N6UkVOUFMyTlhZMXBoY25GQlRUaEJhWFV0WDNoSk4wTm5aSFJaV0U0d1dsaEpkMFZCUmt0TVoyOUtZekpXYW1ORVNURk9iWE40UldsRlJIUlNTRk5zVnpSRGEySlNNbkJVUlRRNVVGOVdja3N6ZFV0aVlVVkRlbGg0VDBod09YaGllbmROUXpnaUxDSmxiV0ZwYkNJNkltRnNhV05sUUdkdFlXbHNMbU52YlNJc0ltRm5aU0k2SWpNd0luMHNJblI1Y0dVaU9sc2lWbVZ5YVdacFlXSnNaVU55WldSbGJuUnBZV3dpWFN3aVFHTnZiblJsZUhRaU9sc2lhSFIwY0hNNlhDOWNMM2QzZHk1M015NXZjbWRjTHpJd01UaGNMMk55WldSbGJuUnBZV3h6WEM5Mk1TSmRmWDAubmpWZEZGa0gzUEstYWZ2Mi16NDAzOG9sYTlHX0d2Y3VrMzBtNzI5LXVFZy1xN3hQVlJqRjV5TU1JekVWSkhfZmxyZjZSaEFtZkp4anNIM2pBRnZLeEEiXX0sIm5vbmNlIjoiY1VKam1OaUExZWljcndHQmlGa1ZpdyJ9.K-nq7_956JDS0Zae2y-FP3K8qoMo-jnaFP4nwvB7DL_DXwpDACJ0VVGDrrZP8KUUl0qt-Y0rpfKiidxBdXKsjg"
  ],
  "connection_id": "39deadba-16f1-4fff-85df-2e446265b122",
  "meta_retries": 5
}
```

7. Ensure that it is in the `PresentationVerified` state.
8. The data is in a JWT format that can be decoded (Example website for decoding https://jwt.io/).