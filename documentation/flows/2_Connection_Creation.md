# Connection Creation

Connections will need to be established between the following entities:
1. Issuer and User in order to receive VCs (Verifiable Credentials).
2. Brand and User in order to request presentations.

## Create Connection Flow

To create a connection, follow these steps:

1. Send a GET request to the `/establish-connection-to-user/` endpoint.
2. Provide both the requestor and user entities api-keys (`requestor-api-key` is either the issuer or brand api key). *Dev note: We can split these up into separate requests if needed.*
4. Upon successful creation, the API will return a response with the newly created connections information.

Example request:

```
curl -X 'GET' \
  'http://129.151.179.222:8000/establish-connection-to-user/' \
  -H 'accept: application/json' \
  -H 'requestor-api-key: brand.VvI2TlftM0M4pZIDWRaLGpOLFMhqgbli' \
  -H 'user-api-key: user.XHi0XgTaNsYBdPCvQfBayYFkOS5NuhKo'
```
Example response:

```
{
  "connection_id": "39deadba-16f1-4fff-85df-2e446265b122",
  "thid": "39deadba-16f1-4fff-85df-2e446265b122",
  "label": "Connection request",
  "my_did": null,
  "their_did": null,
  "role": "Inviter",
  "state": "InvitationGenerated",
  "invitation": {
    "id": "39deadba-16f1-4fff-85df-2e446265b122",
    "type": "https://didcomm.org/out-of-band/2.0/invitation",
    "_from": "did:peer:2.Ez6LSf2vDX9NmKoWer8keWtqBR4unqg3ikCbgZmrLkP5Zn6dJ.Vz6MkuVxk8naWzAQ7sJcV4jvWnFkr9YknL6aLWzxtimdxULMR.SeyJ0IjoiZG0iLCJzIjoiaHR0cDovL2hvc3QuZG9ja2VyLmludGVybmFsOjgwODAvZGlkY29tbSIsInIiOltdLCJhIjpbImRpZGNvbW0vdjIiXX0",
    "invitation_url": "https://my.domain.com/path?_oob=eyJpZCI6IjM5ZGVhZGJhLTE2ZjEtNGZmZi04NWRmLTJlNDQ2MjY1YjEyMiIsInR5cGUiOiJodHRwczovL2RpZGNvbW0ub3JnL291dC1vZi1iYW5kLzIuMC9pbnZpdGF0aW9uIiwiZnJvbSI6ImRpZDpwZWVyOjIuRXo2TFNmMnZEWDlObUtvV2VyOGtlV3RxQlI0dW5xZzNpa0NiZ1ptckxrUDVabjZkSi5WejZNa3VWeGs4bmFXekFRN3NKY1Y0anZXbkZrcjlZa25MNmFMV3p4dGltZHhVTE1SLlNleUowSWpvaVpHMGlMQ0p6SWpvaWFIUjBjRG92TDJodmMzUXVaRzlqYTJWeUxtbHVkR1Z5Ym1Gc09qZ3dPREF2Wkdsa1kyOXRiU0lzSW5JaU9sdGRMQ0poSWpwYkltUnBaR052YlcwdmRqSWlYWDAiLCJib2R5Ijp7ImdvYWxfY29kZSI6ImlvLmF0YWxhcHJpc20uY29ubmVjdCIsImdvYWwiOiJFc3RhYmxpc2ggYSB0cnVzdCBjb25uZWN0aW9uIGJldHdlZW4gdHdvIHBlZXJzIHVzaW5nIHRoZSBwcm90b2NvbCAnaHR0cHM6Ly9hdGFsYXByaXNtLmlvL21lcmN1cnkvY29ubmVjdGlvbnMvMS4wL3JlcXVlc3QnIiwiYWNjZXB0IjpbXX19"
  },
  "created_at": "2024-04-25T12:56:41.851656Z",
  "updated_at": null,
  "meta_retries": 5,
  "kind": "Connection"
}
```

## View Connection
To verify that a connection is created, use the `/view-connection/{id}` endpoint where `{id}` is the `connection_id` returned in the previous step. 

If the connection is up the state field should be `"state": "ConnectionResponseSent"` .