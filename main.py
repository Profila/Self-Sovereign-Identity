from fastapi import FastAPI, Header, HTTPException, Path
from fastapi.responses import JSONResponse
from os import environ as env
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
from swagger_client.rest import ApiException
from models_custom import *
from openapi.models import ConnectionsPage, CredentialSchemaResponse, DIDResolutionResult, EntityCreated, EntityResponse, EntityResponsePage, IssueCredentialRecord, ManagedDIDPage, PresentationStatus, PresentationStatusPage, WalletDetail, WalletDetailPage, Connection
from utils import generate_api_key, serialize, generate_challenge
import time
import logging
import enum

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
]

app = FastAPI(openapi_tags=tags_metadata, title="Profila Prism API", description="API for Prism SSI operations", version="0.1.0")

# Create a Configuration object with a new Prism API URL
config = Configuration()
config.host = env['PRISM_URL']
hostAddress = env['HOST_ADDRESS']

client = ApiClient(config)

class EntityType(enum.Enum):
    USER = "user"
    ISSUER = "issuer"
    BRAND = "brand"

@app.post("/create-entity/{entity_type}", tags=["Admin"])
def create_entity(entity_type: EntityType, request: CreateEntityRequest, x_admin_api_key: str = Header(None)) -> EntityCreated:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Create a wallet
        wallet_api = WalletManagementApi(client)
        walletRes = wallet_api.create_wallet({'name': request.name})

        # Create an entity linked to the wallet
        entityApi = IdentityAndAccessManagementApi(client)
        entityRes = entityApi.create_entity({"name": request.name, "walletId": walletRes.id})

        # Provide Auth method for new entity
        entityApiKey = f"{entity_type.value}." + generate_api_key()
        entityApi.add_entity_api_key_authentication({"entityId": entityRes.id, "apiKey": entityApiKey})

        # Set appropriate purpose based on entity type
        purpose = "authentication" if entity_type == EntityType.USER else "assertionMethod"

        # Create a DID for the entity
        client.set_default_header('apiKey', entityApiKey)
        didApi = DIDRegistrarApi(client)
        didRes = didApi.post_did_registrar_dids({
            "documentTemplate": {
                "publicKeys": [{"id": "auth-1", "purpose": purpose}],
                "services": []
            }
        })

        logger.info(f"Created new {entity_type.value}: {entityRes.id}")

        # Build response with required info from all requests
        response = {
            "entityId": entityRes.id,
            "walletId": walletRes.id,
            "did": didRes.long_form_did,
            "entityApiKey": entityApiKey
        }

        return JSONResponse(content=response, status_code=201)

    except ApiException as e:
        logger.error(f"Exception when processing create_{entity_type.value}: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})

    except Exception as e:
        logger.error(f"Exception when processing create_{entity_type.value}: {e}")
        raise HTTPException(status_code=500)


@app.post("/create-new-entity-api-key/{entity_id}", tags=["Admin"])
def create_entity_api_key(entity_type: EntityType, entity_id: str = Path(..., description="Entity ID"), x_admin_api_key: str = Header(None)) -> NewApiKey:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Create a new API key for the entity
        entityApi = IdentityAndAccessManagementApi(client)
        entityApiKey = f"{entity_type.value}." + generate_api_key()
        entityApi.add_entity_api_key_authentication({"entityId": entity_id, "apiKey": entityApiKey})

        logger.info(f"Created new API key for entity: {entity_id}")

        return {"newApiKey": entityApiKey}

    except ApiException as e:
        logger.error(f"Exception when creating API key for entity: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-all-entities/", tags=["Admin"])
def list_users(x_admin_api_key: str = Header(None)) -> EntityResponsePage:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Access the Identity and Access Management API to retrieve all entities
        entityApi = IdentityAndAccessManagementApi(client)
        users = entityApi.get_all_entities()

        # Return a structured response containing the list of users
        return users

    except ApiException as e:
        # Log the exception and provide a JSON formatted error response
        logger.info(f"Exception when calling the Entity API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    

@app.get("/view-entity/{id}", tags=["Admin"])
def get_entity(id: str = Path(..., description="Entity ID"), x_admin_api_key: str = Header(None)) -> EntityResponse:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Retrieve entity details using the Identity and Access Management API
        entityApi = IdentityAndAccessManagementApi(client)
        entity = entityApi.get_entity_by_id(id)

        # Return a structured response containing the entity details
        return entity

    except ApiException as e:
        # Handle any API exceptions that occur and provide a JSON error response
        logger.info(f"Exception when accessing the entity API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-all-wallets/", tags=["Admin"])
def list_wallets(x_admin_api_key: str = Header(None)) -> WalletDetailPage:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Retrieve list of wallets using the WalletManagement API
        wallet_api = WalletManagementApi(client)
        wallets = wallet_api.get_wallets()

        # Return a structured response with the list of wallets
        return wallets

    except ApiException as e:
        # Handle any API exceptions that occur and provide a JSON error response
        logger.info(f"Exception when accessing the wallet API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/view-wallet/{id}", tags=["Admin"])
def get_wallet(id: str = Path(..., description="Wallet ID"), x_admin_api_key: str = Header(None)) -> WalletDetail:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    try:
        # Retrieve wallet details using the WalletManagement API
        wallet_api = WalletManagementApi(client)
        wallet = wallet_api.get_wallets_walletid(id)

        # Return a structured response containing the wallet details
        return wallet

    except ApiException as e:
        # Handle any API exceptions that occur and provide a JSON error response
        logger.info(f"Exception when accessing the wallet API: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/resolve-did/{did}", tags=["Admin"])
def resolve_did(did: str = Path(..., description="The DID to resolve"), x_admin_api_key: str = Header(None)) -> DIDResolutionResult:
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    didApi = DIDApi(client)

    try:
        res = didApi.get_did(did)
        return res
    except ApiException as e:
        logger.info(f"Exception when calling DIDApi->get_did: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-dids/", tags=["User"])
def list_user_dids(user_api_key: str = Header(None)) -> ManagedDIDPage:
    client.set_default_header('apiKey', user_api_key)

    didRegistrar = DIDRegistrarApi(client)

    try:
        res = didRegistrar.get_did_registrar_dids()
        return res
    except ApiException as e:
        logger.info(f"Exception when calling DIDRegistrarApi->get_did_registrar_dids: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/establish-connection-to-user/", tags=["Issuer", "Brand"])
def establish_connection_to_user(requestor_api_key: str = Header(None), user_api_key: str = Header(None)) -> Connection:
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

        logger.info("User accepting credential: %s\n" % serialize(acceptConnRes))
        logger.info(f"Host: {hostAddress}")
        logger.info(f"Prism URL: {config.host}")

        # Issuer checks connection status
        client.set_default_header('apiKey', requestor_api_key)
        checkConnRes = connectionApi.get_connection(createConnRes.thid)

        logger.info(f"Establish connection: {checkConnRes.connection_id}")

        return checkConnRes
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    except ValueError as ve:
        logger.info(f"Value Error: {ve}")
        raise HTTPException(status_code=400, detail={"reason": str(ve)})
    except Exception as e:
        logger.info(f"Connection exception: {e}")
        raise HTTPException(status_code=500)


@app.get("/view-connection/{id}", tags=["Issuer", "Brand"])
def get_connection(id: str = Path(..., description="Connection ID"), requestor_api_key: str = Header(None)) -> Connection:
    client.set_default_header('apiKey', requestor_api_key)

    connectionApi = ConnectionsManagementApi(client)

    try:
        # Check connection status for a specific ID
        res = connectionApi.get_connection(id)
        return res.to_dict()
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi->get_connection: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-connections/", tags=["Issuer", "Brand"])
def list_connections(requestor_api_key: str = Header(None)) -> ConnectionsPage:
    client.set_default_header('apiKey', requestor_api_key)

    connectionApi = ConnectionsManagementApi(client)

    try:
        # Check connection status
        res = connectionApi.get_connections()
        return res.to_dict()
    except ApiException as e:
        logger.info(f"Exception when calling ConnectionsManagementApi->get_connections: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    
# Create new schema

@app.post("/create-schema/", tags=["Issuer"])
def create_schema(request: CreateSchemaRequest, issuer_did: str, issuer_api_key: str = Header(None)) -> CredentialSchemaResponse:
    client.set_default_header('apiKey', issuer_api_key)

    schemaApi = SchemaRegistryApi(client)

    try:
        # Create Schema

        credential_schema_input = swagger_client.CredentialSchemaInput(
                            name=request.schemaName, 
                            version=request.schemaVersion, 
                            description=request.schemaDescription, 
                            type="https://w3c-ccg.github.io/vc-json-schemas/schema/2.0/schema.json",
                            schema={
                                "$id": request.schemaId,
                                "$schema": "https://json-schema.org/draft/2020-12/schema",
                                "type": "object",
                                "properties": {attr.name: {"type": attr.dataType} for attr in request.attributes},
                                "required": [attr.name for attr in request.attributes],
                                "additionalProperties": False,
                            },
                                tags=request.schemaTags, 
                                author=issuer_did,
                            )

        schemaRes = schemaApi.create_schema(credential_schema_input)

        logger.info(f"Created new schema: {schemaRes.guid}")

        return schemaRes
    except ApiException as e:
        logger.info(f"Exception when calling SchemaRegistryApi->create_schema: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    except Exception as e:
        logger.info(f"Exception when calling SchemaRegistryApi->create_schema: {e}\n")
        raise HTTPException(status_code=500)

# Get Shema by id

@app.get("/view-schema/{id}", tags=["Issuer"])
def get_schema(id: str = Path(..., description="Schema ID"), issuer_api_key: str = Header(None)) -> CredentialSchemaResponse:
    client.set_default_header('apiKey', issuer_api_key)

    schemaApi = SchemaRegistryApi(client)

    try:
        # Get Schema
        schemaRes = schemaApi.get_schema_by_id(id)
        return schemaRes
    except ApiException as e:
        logger.info(f"Exception when calling SchemaRegistryApi->get_schema_by_id: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    

@app.post("/offer-credential/", tags=["Issuer"])
def offer_credential(request: CredentialOfferRequest, schema_id: str, issuer_api_key: str = Header(None)) -> IssueCredentialRecord:
    client.set_default_header('apiKey', issuer_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Create Credential Offer
        offerData = {
            "validityPeriod": 86400,  # One day
            "schemaId": f"http://{hostAddress}:8080/prism-agent/schema-registry/schemas/{schema_id}",
            "issuingDID": request.issuerDid,
            "claims": {
                # loop through claims
                attr.name: attr.value for attr in request.attrClaims
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
                return issuerOfferRes
            time.sleep(1)  # Sleep for 1 second
            issuerOfferRes = issueCredApi.get_credential_record(offerRes.record_id)

        # If state is not OfferSent after retries
        raise HTTPException(status_code=400, detail="Credential offer not sent after 10 retries")

    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->create_credential_offer: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-credential-offers/", tags=["User"])
def list_credential_offers(user_api_key: str = Header(None)) -> List[IssueCredentialRecord]:
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # List Holder Credential Offers
        holderOffersRes = issueCredApi.get_credential_records()
        
        # Filter out the offers that are not in OfferReceived state
        holderOffers = [offer for offer in holderOffersRes.contents if offer.protocol_state == "OfferReceived"]
        
        return holderOffers
    
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_records: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/accept-credential-offer/{id}", tags=["User"])
def accept_credential_offer(subjectId: str, id: str = Path(..., description="Offer ID"), user_api_key: str = Header(None)) -> IssueCredentialRecord:
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Accept Credential Offer
        acceptCredRes = issueCredApi.accept_credential_offer(body={"subjectId": subjectId}, record_id=id)
        return acceptCredRes
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->accept_credential_offer: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    

@app.get("/view-credential/{id}", tags=["User"])
def get_credential(id: str = Path(..., description="Credential ID"), user_api_key: str = Header(None)) -> IssueCredentialRecord:
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # Get Credential Details
        credentialRes = issueCredApi.get_credential_record(id)
        return credentialRes
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_record: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-received-credentials/", tags=["User"])
def list_received_credentials(user_api_key: str = Header(None)) -> List[IssueCredentialRecord]:
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    try:
        # List Holder Credentials
        res = issueCredApi.get_credential_records()

        # Filter out the credentials that are not in CredentialReceived state
        credentials = [credential for credential in res.contents if credential.protocol_state == "CredentialReceived"]

        return credentials
    except ApiException as e:
        logger.info(f"Exception when calling IssueCredentialsProtocolApi->get_credential_records: {e}\n")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.post("/create-presentation-request/", tags=["Brand"])
async def create_presentation_request(connection_id: str, trusted_issuer_did: str, brand_api_key: str = Header(None)) -> PresentationStatus:
    client.set_default_header('apiKey', brand_api_key)
    
    presentationApi = swagger_client.PresentProofApi(client)
    
    # Generate a unique challenge for the request
    challenge = generate_challenge()

    proofData = swagger_client.RequestPresentationInput(
        connection_id=connection_id, 
        options={"challenge": challenge, "domain": "https://profila.com"},
        proofs=[{"schemaId": "https://schema.org/Person", "trustIssuers": [trusted_issuer_did]}]
    )

    try:
        res = presentationApi.request_presentation(proofData)
        logger.info("Presentation request created. Request ID: %s\n" % res.presentation_id)

        return res
    except swagger_client.ApiException as e:
        logger.info(f"Exception when calling PresentProofApi->request_presentation: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/list-presentation-requests/", tags=["User", "Brand"])
async def list_presentation_requests(requestor_api_key: str = Header(None)) -> PresentationStatusPage:
    client.set_default_header('apiKey', requestor_api_key)
    
    presentationApi = swagger_client.PresentProofApi(client)
    
    try:
        res = presentationApi.get_all_presentation()
        return res
    except swagger_client.ApiException as e:
        logger.info(f"Exception when calling PresentProofApi->get_all_presentation: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/view-presentation-request/{id}", tags=["User", "Brand"])
async def get_presentation_request(id: str = Path(..., description="Presentation Request ID"), requestor_api_key: str = Header(None)) -> PresentationStatus:
    client.set_default_header('apiKey', requestor_api_key)

    presentationApi = swagger_client.PresentProofApi(client)

    try:
        res = presentationApi.get_presentation(id)
        return res
    except swagger_client.ApiException as e:
        logger.info(f"Exception when calling PresentProofApi->get_presentation: {e}")
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
    

@app.post("/present-credential/{id}", tags=["User"])
def present_credential(vc_record_id: str, id: str = Path(..., description="Presentation Request ID"), user_api_key: str = Header(None)) -> PresentationStatus:
    client.set_default_header('apiKey', user_api_key)

    presentationApi = PresentProofApi(client)

    # Respond to Presentation Request

    body = swagger_client.RequestPresentationAction(action="request-accept", proof_id=[vc_record_id])
    
    try:
        res = presentationApi.update_presentation(body=body, presentation_id=id)
        logger.info("Presented credential: %s\n" % serialize(res))
        return res
    except ApiException as e:
        logger.info("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})
