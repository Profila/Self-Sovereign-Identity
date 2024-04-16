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
from swagger_client.api.issue_credentials_protocol_api import IssueCredentialsProtocolApi
from swagger_client.configuration import Configuration
from models import *
from utils import generate_api_key


tags_metadata = [
    {
        "name": "Admin",
        "description": "Endpoints available only to admin users (Requires admin api key)."
    },
    {
        "name": "User",
        "description": "Endpoints accessible by regular users (Requires user api key)."
    },
    {
        "name": "Issuer",
        "description": "Endpoints for issuer interactions. (Requires issuer api key)."
    },
    {
        "name": "General",
        "description": "Endpoints for general interactions. (Requires no api key)."
    },

]

app = FastAPI(openapi_tags=tags_metadata, title="Profila Prism API", description="API for Prism SSI operations", version="0.1.0")

# Create a Configuration object with a new Prism API URL
config = Configuration()
config.host = env['PRISM_URL']
hostAddress = env['HOST_ADDRESS']

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

    # Resolve a DID

    didApi = DIDApi(client)

    res = didApi.get_did(did)

    return res


@app.get("/admin/user-details/{id}", tags=["Admin"])
def user_details(id: str = Path(..., description="User ID"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # Show user details

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_entity_by_id(id)

    return res

@app.get("/user/list-dids/", tags=["User"])
def list_user_dids(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    # List all dids of user

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

@app.post("/issuer/issue-credential", tags=["Issuer"])
def issue_credential(request: CredentialOfferRequest, user_api_key: str = Header(None), issuer_api_key: str = Header(None)):
    client.set_default_header('apiKey', issuer_api_key)

    # Create Credential Offer

    issueCredApi = IssueCredentialsProtocolApi(client)

    offerRes = issueCredApi.create_credential_offer({"validityPeriod": 86400, # One day
                                                     "schemaId": "http://"+hostAddress+":8080/prism-agent/schema-registry/schemas/fa313f8f-0c93-35d2-b65d-364e656bd9cf",
                                                     "credentialDefinitionId": "39790594-d09d-3865-b2a3-d0e8ea6ffa77",
                                                     "issuingDID": request.issuerDid,
                                                     "credential_format": "AnonCreds",
                                                     "claims": {"email": request.email, "name": request.name, "surname": request.surname},
                                                     "connectionId": request.connectionId,
                                                     "credentialFormat": "AnonCreds"})

    return offerRes


@app.get("/get-profile-schema/", tags=["General"])
def get_schema():

    # Get profile schema

    schemaApi = SchemaRegistryApi(client)

    res = schemaApi.get_schema_by_id("fa313f8f-0c93-35d2-b65d-364e656bd9cf")

    return res