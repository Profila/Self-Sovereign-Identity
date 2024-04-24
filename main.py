from fastapi import FastAPI, Header, HTTPException, Path
from fastapi.responses import JSONResponse
from os import environ as env
from pprint import pprint
import swagger_client
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
from swagger_client.api.present_proof_api import PresentProofApi
import swagger_client.models
from swagger_client.rest import ApiException
from models import *
from utils import generate_api_key, serialize
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Logs will be written to this file
    filemode='a')

logger = logging.getLogger(__name__)

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
        "name": "Brand",
        "description": "Endpoints for brand interactions. (Requires brand api key)."
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

@app.get("/get-profile-schema/", tags=["General"])
def get_schema():
    try:
        # Initialize the Schema Registry API client
        schemaApi = SchemaRegistryApi(client)

        # Fetch the schema using a predefined schema ID
        schema_id = "fa313f8f-0c93-35d2-b65d-364e656bd9cf"
        schema = schemaApi.get_schema_by_id(schema_id)

        # Return the schema information in a standardized JSON format
        return JSONResponse(content={"schema": schema}, status_code=200)

    except ApiException as e:
        # Log the ApiException and return a JSON formatted error response
        logger.info(f"Failed to retrieve schema: {e}")
        raise HTTPException(status_code=e.status, detail={"error": e.reason})


@app.get("/list-users", tags=["Admin"])
def list_users(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Access the Identity and Access Management API to retrieve all entities
        entityApi = IdentityAndAccessManagementApi(client)
        users = entityApi.get_all_entities()

        # Return a structured response containing the list of users
        return JSONResponse(content={"users": users}, status_code=200)

    except ApiException as e:
        # Log the exception and provide a JSON formatted error response
        logger.info(f"Exception when calling the Entity API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-wallets", tags=["Admin"])
def list_wallets(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Retrieve list of wallets using the WalletManagement API
        wallet_api = WalletManagementApi(client)
        wallets = wallet_api.get_wallets()

        # Return a structured response with the list of wallets
        return JSONResponse(content={"wallets": wallets}, status_code=200)

    except ApiException as e:
        # Handle any API exceptions that occur and provide a JSON error response
        logger.info(f"Exception when accessing the wallet API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/create-user", tags=["Admin"])
def create_user(request: CreateUserRequest, x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Create a wallet
        wallet_api = WalletManagementApi(client)
        walletRes = wallet_api.create_wallet({'name': request.name})

        # Create an entity linked to the wallet
        entityApi = IdentityAndAccessManagementApi(client)
        entityRes = entityApi.create_entity({"name": request.name, "walletId": walletRes.id})

        # Provide Auth method for new entity
        userApiKey = "user." + generate_api_key()
        entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

        # Create a DID for the entity
        client.set_default_header('apiKey', userApiKey)
        didApi = DIDRegistrarApi(client)
        didRes = didApi.post_did_registrar_dids({
            "documentTemplate": {
                "publicKeys": [{"id": "auth-1", "purpose": "authentication"}],
                "services": []
            }
        })

        # Build response with required info from all requests
        response = {
            "userId": entityRes.id,
            "walletId": walletRes.id,
            "did": didRes.long_form_did,
            "userApiKey": userApiKey
        }
        return JSONResponse(content=response, status_code=201)

    except ApiException as e:
        logger.info(f"Exception when processing create_user: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/create-issuer", tags=["Admin"])
def create_issuer(request: CreateUserRequest, x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Create a wallet
        wallet_api = WalletManagementApi(client)
        walletRes = wallet_api.create_wallet({'name': request.name})

        # Create an entity linked to the wallet
        entityApi = IdentityAndAccessManagementApi(client)
        entityRes = entityApi.create_entity({"name": request.name, "walletId": walletRes.id})

        # Provide Auth method for new entity
        userApiKey = "issuer." + generate_api_key()
        entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

        # Create a DID for the entity
        client.set_default_header('apiKey', userApiKey)
        didApi = DIDRegistrarApi(client)
        didRes = didApi.post_did_registrar_dids({
            "documentTemplate": {
                "publicKeys": [{"id": "auth-1", "purpose": "assertionMethod"}],
                "services": []
            }
        })

        # Build response with required info from all requests
        response = {
            "userId": entityRes.id,
            "walletId": walletRes.id,
            "did": didRes.long_form_did,
            "userApiKey": userApiKey
        }
        return JSONResponse(content=response, status_code=201)

    except ApiException as e:
        logger.info(f"Exception when processing create_issuer: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/create-brand", tags=["Admin"])
def create_brand(request: CreateUserRequest, x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Create a wallet
        wallet_api = WalletManagementApi(client)
        walletRes = wallet_api.create_wallet({'name': request.name})

        # Create an entity linked to the wallet
        entityApi = IdentityAndAccessManagementApi(client)
        entityRes = entityApi.create_entity({"name": request.name, "walletId": walletRes.id})

        # Provide Auth method for new entity
        userApiKey = "brand." + generate_api_key()
        entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": userApiKey})

        # Create a DID for the entity
        client.set_default_header('apiKey', userApiKey)
        didApi = DIDRegistrarApi(client)
        didRes = didApi.post_did_registrar_dids({
            "documentTemplate": {
                "publicKeys": [{"id": "auth-1", "purpose": "assertionMethod"}],
                "services": []
            }
        })

        # Build response with required info from all requests
        response = {
            "userId": entityRes.id,
            "walletId": walletRes.id,
            "did": didRes.long_form_did,
            "userApiKey": userApiKey
        }
        return JSONResponse(content=response, status_code=201)

    except ApiException as e:
        logger.info(f"Exception when processing create_brand: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})



@app.get("/resolve-did/{did}", tags=["Admin"])
def resolve_did(did: str = Path(..., description="The DID to resolve"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    didApi = DIDApi(client)

    try:
        res = didApi.get_did(did)
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling DIDApi->get_did: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/user-details/{id}", tags=["Admin"])
def user_details(id: str = Path(..., description="User ID"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    entityApi = IdentityAndAccessManagementApi(client)

    try:
        res = entityApi.get_entity_by_id(id)
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling IdentityAndAccessManagementApi->get_entity_by_id: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-dids/", tags=["User"])
def list_user_dids(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    didRegistrar = DIDRegistrarApi(client)

    try:
        res = didRegistrar.get_did_registrar_dids()
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling DIDRegistrarApi->get_did_registrar_dids: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/establish-connection-to-user/", tags=["Issuer", "Brand"])
def establish_connection_to_user(requestor_api_key: str = Header(None), user_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

    connectionApi = ConnectionsManagementApi(client)

    try:
        # Issuer creates an invitation
        createConnRes = connectionApi.create_connection({"label": "Connection request"})
        invitation_url = createConnRes.invitation.invitation_url
        rawInvitation = invitation_url.split('oob=')[1] if 'oob=' in invitation_url else None

        if not rawInvitation:
            raise ValueError("Invalid invitation URL format.")

        # User accepts the invitation
        client.set_default_header('apiKey', user_api_key)
        acceptConnRes = connectionApi.accept_connection_invitation({"invitation": rawInvitation})

        # Issuer checks connection status
        client.set_default_header('apiKey', requestor_api_key)
        checkConnRes = connectionApi.get_connection(createConnRes.thid)

        return JSONResponse(content=checkConnRes, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    except ValueError as ve:
        logger.info(f"Value Error: {ve}")
        raise HTTPException(status_code=400, detail={"reason": str(ve)})


@app.get("/check-connection/{id}", tags=["Issuer", "Brand"])
def check_connection(id: str = Path(..., description="Connection ID"), requestor_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

    connectionApi = ConnectionsManagementApi(client)

    try:
        # Check connection status for a specific ID
        res = connectionApi.get_connection(id)
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi->get_connection: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-connections/", tags=["Issuer", "Brand"])
def list_connections(requestor_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

    connectionApi = ConnectionsManagementApi(client)

    try:
        # Check connection status
        res = connectionApi.get_connections()
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi->get_connections: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/offer-credential", tags=["Issuer"])
def offer_credential(request: CredentialOfferRequest, schema_id: str, issuer_api_key: str = Header(None)):
    client.set_default_header('apiKey', issuer_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Create Credential Offer
        offerData = {
            "validityPeriod": 86400,  # One day
            "schemaId": f"http://{hostAddress}:8080/prism-agent/schema-registry/schemas/{schema_id}",
            "issuingDID": request.issuerDid,
            "claims": {
                "emailAddress": request.email, 
                "givenName": request.name, 
                "familyName": request.surname
            },
            "automaticIssuance": True,
            "connectionId": request.connectionId,
            "credentialFormat": "JWT"
        }
        offerRes = issueCredApi.create_credential_offer(offerData)

        # Polling to check credential offer state
        issuerOfferRes = issueCredApi.get_credential_record(offerRes.record_id)
        retries = 10
        for _ in range(retries):
            if issuerOfferRes.protocol_state == "OfferSent":
                return JSONResponse(content=issuerOfferRes, status_code=200)
            time.sleep(1)  # Sleep for 1 second
            issuerOfferRes = issueCredApi.get_credential_record(offerRes.record_id)

        # If state is not OfferSent after retries
        raise HTTPException(status_code=400, detail="Credential offer not sent after 10 retries")

    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->create_credential_offer: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-credential-offers", tags=["User"])
def list_credential_offers(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # List Holder Credential Offers
        holderOffersRes = issueCredApi.get_credential_records()
        
        # Filter out the offers that are not in OfferReceived state
        holderOffers = [offer for offer in holderOffersRes.contents if offer.protocol_state == "OfferReceived"]
        
        return JSONResponse(content={"offers": holderOffers}, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_records: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/accept-credential-offer/{id}", tags=["User"])
def accept_credential_offer(subjectId: str, id: str = Path(..., description="Offer ID"), user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Accept Credential Offer
        acceptCredRes = issueCredApi.accept_credential_offer(body={"subjectId": subjectId}, record_id=id)
        return JSONResponse(content=acceptCredRes, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->accept_credential_offer: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    

@app.get("/get-credential/{id}", tags=["User"])
def get_credential(id: str = Path(..., description="Credential ID"), user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Get Credential Details
        credentialRes = issueCredApi.get_credential_record(id)
        return JSONResponse(content=credentialRes, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_record: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-credentials/", tags=["User"])
def list_credentials(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # List Holder Credentials
        res = issueCredApi.get_credential_records()
        return JSONResponse(content=res, status_code=200)
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_records: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/create-presentation-request/", tags=["Brand"])
async def create_presentation_request(connection_id: str, trusted_issuer_did: str, brand_api_key: str = Header(None)):
    client.set_default_header('apiKey', brand_api_key)
    
    presentationApi = swagger_client.PresentProofApi(client)
    
    # Generate a unique challenge for the request
    challenge = str(uuid.uuid4())

    proofData = swagger_client.RequestPresentationInput(
        connection_id=connection_id, 
        options={"challenge": challenge, "domain": "https://profila.com"},
        proofs=[{"schemaId": "https://schema.org/Person", "trustIssuers": [trusted_issuer_did]}]
    )

    try:
        res = presentationApi.request_presentation(proofData)
        return JSONResponse(content=res, status_code=200)
    except swagger_client.ApiException as e:
        logger.info(f"Exception when calling PresentProofApi->request_presentation: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-presentation-requests/", tags=["User", "Brand"])
async def list_presentation_requests(requestor_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)
    
    presentationApi = swagger_client.PresentProofApi(client)
    
    try:
        res = presentationApi.get_all_presentation()
        return JSONResponse(content=res, status_code=200)
    except swagger_client.ApiException as e:
        logger.info(f"Exception when calling PresentProofApi->get_all_presentation: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/present-credential/", tags=["User"])
def present_credential(vc_id: str, user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    presentationApi = PresentProofApi(client)

    # Respond to Presentation Request

    body = swagger_client.RequestPresentationAction(action="request-accept", proof_id=[vc_id])
    
    try:
        res = presentationApi.update_presentation(body=body, presentation_id="291cbbab-8e32-49c5-b2e8-423e3590ac08")
        logger.info(serialize(res))
        return JSONResponse(content=serialize(res), status_code=200)
    except ApiException as e:
        logger.info("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/accept-presentation-response/", tags=["Brand"])
def accept_presentation_response(presentation_id: str, brand_api_key: str = Header(None)):
    client.set_default_header('apiKey', brand_api_key)

    presentationApi = PresentProofApi(client)

    body = swagger_client.RequestPresentationAction(action="presentation-accept")

    try:
        res = presentationApi.update_presentation(body=body, presentation_id=presentation_id)
        logger.info(serialize(res))
        return JSONResponse(content=serialize(res), status_code=200)
    except ApiException as e:
        logger.info("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})