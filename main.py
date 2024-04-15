from fastapi import FastAPI, Header, HTTPException, Path
from os import environ as env
from swagger_client import ApiClient
from swagger_client.api.did_api import DIDApi
from swagger_client.api.wallet_management_api import WalletManagementApi
from swagger_client.api.identity_and_access_management_api import IdentityAndAccessManagementApi
from swagger_client.api.did_registrar_api import DIDRegistrarApi
from swagger_client.api.did_api import DIDApi
from swagger_client.api.connections_management_api import ConnectionsManagementApi
from swagger_client.api.schema_registry_api import SchemaRegistryApi
from swagger_client.configuration import Configuration
from models import *
from utils import generate_api_key


tags_metadata = [
    {
        "name": "Admin",
        "description": "Operations available only to admin users (Requires admin api key)."
    },
    {
        "name": "User",
        "description": "Endpoints accessible by regular users (Requires user api key)."
    },
    {
        "name": "Issuer",
        "description": "APIs for issuer interactions. (Requires issuer api key)."
    },
    {
        "name": "General",
        "description": "APIs for general interactions. (Requires no api key)."
    },

]

app = FastAPI(openapi_tags=tags_metadata)

# Create a Configuration object with a new API base URL
config = Configuration()
config.host = env['BASE_URL']

client = ApiClient(config)


@app.get("/admin/list-users", tags=["Admin"])
def list_users(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # List all entities

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_all_entities()

    return res


@app.get("/admin/list-wallets", tags=["Admin"])
def list_wallets(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    wallet_api = WalletManagementApi(client)

    res = wallet_api.get_wallets()

    return res


@app.post("/admin/create-user", tags=["Admin"])
def create_user(request: CreateUserRequest,  x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # Create a wallet
    wallet_api = WalletManagementApi(client)
    walletRes = wallet_api.create_wallet({'name': request.name})
    print("id")
    print(walletRes.id)

    # Create an entity linked to the wallet
    entityApi = IdentityAndAccessManagementApi(client)

    entityRes = entityApi.create_entity({"name": request.name,"walletId": walletRes.id})
    print("entity")
    print(entityRes)

    # Provide Auth method for new entity
    userApiKey = "user." + generate_api_key()
    print("User api key")
    print(userApiKey)
    entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

    # Create a DID for the entity
    client.set_default_header('apiKey', userApiKey)

    didApi = DIDRegistrarApi(client)

    didRes = didApi.post_did_registrar_dids({"documentTemplate": {"publicKeys": [{"id": "auth-1","purpose": "authentication"}],"services": []}})

    # Build response with required info from all requests
    response = {"userId": entityRes.id, "walletId": walletRes.id, "did":didRes.long_form_did, "userApiKey": userApiKey}

    return response

@app.post("/admin/create-issuer", tags=["Admin"])
def create_issuer(request: CreateUserRequest,  x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # Create a wallet
    wallet_api = WalletManagementApi(client)
    walletRes = wallet_api.create_wallet({'name': request.name})
    print("id")
    print(walletRes.id)

    # Create an entity linked to the wallet
    entityApi = IdentityAndAccessManagementApi(client)

    entityRes = entityApi.create_entity({"name": request.name,"walletId": walletRes.id})
    print("entity")
    print(entityRes)

    # Provide Auth method for new entity
    userApiKey = "issuer." + generate_api_key()
    print("User api key")
    print(userApiKey)
    entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

    # Create a DID for the entity
    client.set_default_header('apiKey', userApiKey)

    didApi = DIDRegistrarApi(client)

    didRes = didApi.post_did_registrar_dids({"documentTemplate": {"publicKeys": [{"id": "auth-1","purpose": "assertionMethod"}],"services": []}})

    # Build response with required info from all requests
    response = {"userId": entityRes.id, "walletId": walletRes.id, "did":didRes.long_form_did, "userApiKey": userApiKey}

    return response


@app.get("/admin/resolve-did/{did}", tags=["Admin"])
def resolve_did(did: str = Path(..., description="The DID to resolve"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # List all entities

    didApi = DIDApi(client)

    res = didApi.get_did(did)

    return res


@app.get("/admin/user-details/{id}", tags=["Admin"])
def user_details(id: str = Path(..., description="User ID"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # List all entities

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_entity_by_id(id)

    return res

@app.get("/user/list-dids/", tags=["User"])
def list_user_dids(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    # List all entities

    didRegistrar = DIDRegistrarApi(client)

    res = didRegistrar.get_did_registrar_dids()

    return res

# For Connection Testing

# Issuer api key:
# issuer.C'W&|x5X0A_v&g81Fk=D_r~79&B|9(#/

# Issuer did:
# did:prism:7ee249c59b514692080bb9594f73660cf1b646857004b5b6dbd7e9f0b4e4a6ae:CnsKeRI6CgZhdXRoLTEQAkouCglzZWNwMjU2azESIQIso2BYlVFFre5z2RuSvhMC69_rLsB-v48JxlA_XesimxI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiECSV3EYmK50xxA6lKRdnq364EN3ccFCCoUE9O0z_uu9sQ

# Issuer ID:
# 3ee7729e-c682-44d7-97ab-3913899a9807

# User api key:
# user.Ch.IXJS:Erf}jWF7LKHDYBtq4Na8C0?p

# User did:
# did:prism:36b17296f475a6ad745ce47e02444387528fd448d50bfc3210b6121679cf5125:CnsKeRI6CgZhdXRoLTEQBEouCglzZWNwMjU2azESIQK0Ey3UOzwYvill4tOqLyKKuPeF8IvG9LeMV9V61Jo6rxI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiEDTa2hhs_byweaq0no6v4Rg95ygcY51tfu6aSdx-PKAbs

# User ID:
# 8bd47798-f4e0-423a-a83c-af938b89b6e5

@app.get("/issuer/establish-issuer-to-user-connection/", tags=["Issuer"])
def establish_connection_issuer_to_user(user_api_key: str = Header(None), issuer_api_key: str = Header(None)):
    client.set_default_header('apiKey', issuer_api_key)

    # Establish a didcomm connection

    connectionApi = ConnectionsManagementApi(client)

    # Issuer Create Invitation
    createConnRes = connectionApi.create_connection({"label": "Connection request"})

    # User Accept Invitation
    client.set_default_header('apiKey', user_api_key)
        # Copy string in createConnRes.invitation.invitationUrl from 'oob=' to the end and store it in rawInvitation
    rawInvitation = createConnRes.invitation.invitation_url.split('oob=')[1]
    acceptConnRes = connectionApi.accept_connection_invitation({"invitation": rawInvitation})

    # Isuer Check Connection Status
    client.set_default_header('apiKey', issuer_api_key)
    checkConnRes = connectionApi.get_connection(createConnRes.thid)

    return checkConnRes

# For Connection Testing
# ID: ab11efb0-1955-4b49-a90c-f72ccc45e412
@app.get("/issuer/check-connection/{id}", tags=["Issuer"])
def check_connection(id: str = Path(..., description="Connection ID"), issuer_api_key: str = Header(None)):
    client.set_default_header('apiKey', issuer_api_key)

    # Check connection status

    connectionApi = ConnectionsManagementApi(client)

    # Issuer Check Connection Status
    res = connectionApi.get_connection(id)

    return res


# Profile Schema:

# {
#     "guid": "3f9a5c9e-2743-3e4f-bbdb-861ed8b2198a",
#     "id": "39f8f184-b888-490a-91ce-d042e1d622e5",
#     "longId": "did:prism:7ee249c59b514692080bb9594f73660cf1b646857004b5b6dbd7e9f0b4e4a6ae:CnsKeRI6CgZhdXRoLTEQAkouCglzZWNwMjU2azESIQIso2BYlVFFre5z2RuSvhMC69_rLsB-v48JxlA_XesimxI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiECSV3EYmK50xxA6lKRdnq364EN3ccFCCoUE9O0z_uu9sQ/39f8f184-b888-490a-91ce-d042e1d622e5?version=1.0.0",
#     "name": "user-profile",
#     "version": "1.0.0",
#     "tags": [
#         "user",
#         "profile"
#     ],
#     "description": "User Profile Schema",
#     "type": "https://w3c-ccg.github.io/vc-json-schemas/schema/2.0/schema.json",
#     "schema": {
#         "$id": "https://profila.com/user-profile-1.0.0",
#         "$schema": "https://json-schema.org/draft/2020-12/schema",
#         "description": "Driving License",
#         "type": "object",
#         "properties": {
#             "emailAddress": {
#                 "type": "string",
#                 "format": "email"
#             },
#             "givenName": {
#                 "type": "string"
#             },
#             "familyName": {
#                 "type": "string"
#             }
#         },
#         "required": [
#             "emailAddress",
#             "familyName",
#             "givenName"
#         ],
#         "additionalProperties": true
#     },
#     "author": "did:prism:7ee249c59b514692080bb9594f73660cf1b646857004b5b6dbd7e9f0b4e4a6ae:CnsKeRI6CgZhdXRoLTEQAkouCglzZWNwMjU2azESIQIso2BYlVFFre5z2RuSvhMC69_rLsB-v48JxlA_XesimxI7CgdtYXN0ZXIwEAFKLgoJc2VjcDI1NmsxEiECSV3EYmK50xxA6lKRdnq364EN3ccFCCoUE9O0z_uu9sQ",
#     "authored": "2024-04-14T08:59:58.292439Z",
#     "kind": "CredentialSchema",
#     "self": "/schema-registry/schemas/3f9a5c9e-2743-3e4f-bbdb-861ed8b2198a"
# }

@app.get("/get-schema/", tags=["General"])
def get_schema():

    # Get profile schema

    schemaApi = SchemaRegistryApi(client)

    res = schemaApi.get_schema_by_id("06407e4f-0826-303b-b101-6fb4276bd467")

    return res