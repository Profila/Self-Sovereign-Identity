from fastapi import FastAPI, Header, HTTPException
from os import environ as env
from swagger_client import ApiClient
from swagger_client.api.did_api import DIDApi
from swagger_client.api.wallet_management_api import WalletManagementApi
from swagger_client.api.identity_and_access_management_api import IdentityAndAccessManagementApi
from swagger_client.api.did_registrar_api import DIDRegistrarApi
from swagger_client.configuration import Configuration
from models import *

app = FastAPI()

# Create a Configuration object with a new API base URL
config = Configuration()
config.host = env['BASE_URL']

client = ApiClient(config)


@app.get("/list-users")
def list_users():
    client.set_default_header('x-admin-api-key', env['ADMIN_API_KEY'])

    # List all entities

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_all_entities()

    return res


@app.get("/list-wallets")
def list_wallets():

    wallet_api = WalletManagementApi(client)

    res = wallet_api.get_wallets()

    return res


@app.post("/create-user")
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
    userApiKey = "user." + entityRes.id
    print("User api key")
    print(userApiKey)
    entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

    # Create a DID for the entity
    client.set_default_header('apiKey', userApiKey)

    didApi = DIDRegistrarApi(client)

    didRes = didApi.post_did_registrar_dids({"documentTemplate": {"publicKeys": [{"id": "auth-1","purpose": "authentication"}],"services": []}})

    # Build response with required info from all requests
    response = {"userId": entityRes.id, "walletId": walletRes.id, "did":didRes.long_form_did}

    return response
