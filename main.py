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
from swagger_client.rest import ApiException
from models import *
from utils import generate_api_key, serialize
import time


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

    # Get profile schema

    schemaApi = SchemaRegistryApi(client)

    res = schemaApi.get_schema_by_id("fa313f8f-0c93-35d2-b65d-364e656bd9cf")

    return res

@app.get("/list-users", tags=["Admin"])
def list_users(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # List all entities

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_all_entities()

    return res


@app.get("/list-wallets", tags=["Admin"])
def list_wallets(x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    wallet_api = WalletManagementApi(client)

    res = wallet_api.get_wallets()

    return res


@app.post("/create-user", tags=["Admin"])
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

@app.post("/create-issuer", tags=["Admin"])
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

@app.post("/create-brand", tags=["Admin"])
def create_brand(request: CreateUserRequest,  x_admin_api_key: str = Header(None)):
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
    userApiKey = "brand." + generate_api_key()
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


@app.get("/resolve-did/{did}", tags=["Admin"])
def resolve_did(did: str = Path(..., description="The DID to resolve"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # Resolve a DID

    didApi = DIDApi(client)

    res = didApi.get_did(did)

    return res


@app.get("/user-details/{id}", tags=["Admin"])
def user_details(id: str = Path(..., description="User ID"), x_admin_api_key: str = Header(None)):
    client.set_default_header('x-admin-api-key', x_admin_api_key)

    # Show user details

    entityApi = IdentityAndAccessManagementApi(client)

    res = entityApi.get_entity_by_id(id)

    return res

@app.get("/list-dids/", tags=["User"])
def list_user_dids(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    # List all dids of user

    didRegistrar = DIDRegistrarApi(client)

    res = didRegistrar.get_did_registrar_dids()

    return res


@app.get("/establish-connection-to-user/", tags=["Issuer", "Brand"])
def establish_connection_to_user(requestor_api_key: str = Header(None), user_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

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
    client.set_default_header('apiKey', requestor_api_key)
    checkConnRes = connectionApi.get_connection(createConnRes.thid)

    return checkConnRes

@app.get("/check-connection/{id}", tags=["Issuer", "Brand"])
def check_connection(id: str = Path(..., description="Connection ID"), requestor_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

    # Check connection status

    connectionApi = ConnectionsManagementApi(client)

    # Issuer Check Connection Status
    res = connectionApi.get_connection(id)

    return res

@app.get("/list-connections/", tags=["Issuer", "Brand"])
def list_connections(requestor_api_key: str = Header(None)):
    client.set_default_header('apiKey', requestor_api_key)

    # Check connection status

    connectionApi = ConnectionsManagementApi(client)

    # Issuer Check Connection Status
    res = connectionApi.get_connections()

    return res

@app.post("/offer-credential", tags=["Issuer"])
def offer_credential(request: CredentialOfferRequest, user_api_key: str = Header(None), issuer_api_key: str = Header(None)):
    client.set_default_header('apiKey', issuer_api_key)

    # Create Credential Offer

    issueCredApi = IssueCredentialsProtocolApi(client)

    # {
    #     "claims": {
    #     "emailAddress": "alice@wonderland.com",
    #     "givenName": "Alice",
    #     "familyName": "Wonderland",
    #     "dateOfIssuance": "2020-11-13T20:20:39+00:00",
    #     "drivingLicenseID": "12345",
    #     "drivingClass": 3
    #     },
    #     "credentialFormat": "JWT",
    #     "issuingDID": "did:prism:9f847f8bbb66c112f71d08ab39930d468ccbfe1e0e1d002be53d46c431212c26",
    #     "connectionId": "9d075518-f97e-4f11-9d10-d7348a7a0fda",
    #     "schemaId": "http://localhost:8080/prism-agent/schema-registry/schemas/3f86a73f-5b78-39c7-af77-0c16123fa9c2"
    # }

    # TODO Elmer: Use model
    offerRes = issueCredApi.create_credential_offer({"validityPeriod": 86400, # One day
                                                     "schemaId": "http://"+hostAddress+":8080/prism-agent/schema-registry/schemas/c02e2e89-b7fe-3c78-a4e3-3bc6636b5469",
                                                     "issuingDID": request.issuerDid,
                                                     "claims": {"emailAddress": request.email, "givenName": request.name, "familyName": request.surname},
                                                     "automaticIssuance": True,
                                                     "connectionId": request.connectionId,
                                                     "credentialFormat": "JWT"})
    
    # Record ID: 10c766af-8cea-4a81-8a24-99f9051076a5

    issuerOfferRes = issueCredApi.get_credential_record(offerRes.record_id)


    issuerOfferState = issuerOfferRes.protocol_state
    retries = 10
    retryCount = 0
    while issuerOfferState != "OfferSent" and retryCount < retries:
        issuerOfferRes = issueCredApi.get_credential_record(offerRes.record_id)
        issuerOfferState = issuerOfferRes.protocol_state
        # Sleep for 1 second
        time.sleep(1)
        retryCount += 1

    if issuerOfferState != "OfferSent":
        return {"error": "Credential offer not sent"}
    
    return issuerOfferRes

@app.get("/list-credential-offers", tags=["User"])
def list_credential_offers(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)
    # List Holder Credential Offers

    holderOffersRes = issueCredApi.get_credential_records()

    # Filter out the offers that are not in OfferReceived state

    holderOffers = []
    for offer in holderOffersRes.contents:
        if(offer.protocol_state == "OfferReceived"):
            holderOffers.append(offer)

    # Accept All Credential Offers

    # for offer in holderOffersRes.results:
    #     if(offer.protocol_state == "OfferReceived"):
    #         print("Accepting credential offer")
    #         acceptCredRes = issueCredApi.accept_credential_offer(body={}, record_id=offer.record_id)

    # acceptCredRes = issueCredApi.accept_credential_offer(body={}, record_id="e2d8d813-7bbb-48c6-9b3c-ef03d75b231f")#holderOfferRes.record_id)

    return holderOffers

@app.post("/accept-credential-offer/{id}", tags=["User"])
def accept_credential_offer(subjectId: str, id: str = Path(..., description="Offer ID") , user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    # Accept Credential Offer

    acceptCredRes = issueCredApi.accept_credential_offer(body={"subjectId": subjectId}, record_id=id, )

    return acceptCredRes

@app.get("/get-credential/{id}", tags=["User"])
def get_credential(id: str = Path(..., description="Credential ID") , user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    # Get Credential Details

    credentialRes = issueCredApi.get_credential_record(id)

    return credentialRes



@app.get("/list-credentials/", tags=["User"])
def list_credentials(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    issueCredApi = IssueCredentialsProtocolApi(client)

    # List Holder Credentials

    res = issueCredApi.get_credential_records()

    return res


@app.get("/create-presentation-request/", tags=["Brand"])
def create_presentation_request(brand_api_key: str = Header(None)):
    client.set_default_header('apiKey', brand_api_key)

    presentationApi = PresentProofApi(client)

    # Create Presentation Request

    # proof_request = RequestPresentationInput.from_dict(data)
    # verifier_proof_request: Response[RequestPresentationInput] = request_presentation.sync(client=verifier_client, json_body=proof_request)
    
    # proofData = swagger_client.RequestPresentationInput(connection_id="21ce6a37-122c-426d-b10c-401965942f1b", 
    #                                                     options={"challenge": "11c91493-01b3-4c4d-ac36-b336bab5bddf", 
    #                                                              "domain": "https://example-verifier.com"}, 
    #                                                     proofs=[],
    #                                                     credential_format= "JWT"
    #                                                     )
    proofData = swagger_client.RequestPresentationInput(connection_id="21ce6a37-122c-426d-b10c-401965942f1b", 
                                                        options={"challenge": "11c91493-01b3-4c4d-ac36-b336bab5bddf", 
                                                                 "domain": "https://example-verifier.com"}, 
                                                        proofs=[{"schemaId":"https://schema.org/Person", 
                                                                 "trustIssuers": ["did:prism:cc523481a6540d7c1674a5ecf94ad482619405664cc48d7b14620cf2ef097c12"]}],
                                                        )


    res = presentationApi.request_presentation(proofData)

    return res

@app.get("/present-credential/", tags=["User"])
def present_credential(user_api_key: str = Header(None)):
    client.set_default_header('apiKey', user_api_key)

    presentationApi = PresentProofApi(client)

    # Respond to Presentation Request

    body = swagger_client.RequestPresentationAction(action="request-accept", proof_id=["10781032-d1f0-423e-b050-30d510cdbe51"])
    
    try:
        res = presentationApi.update_presentation(body=body, presentation_id="291cbbab-8e32-49c5-b2e8-423e3590ac08")
        pprint(serialize(res))
        return JSONResponse(content=serialize(res), status_code=200)
    except ApiException as e:
        print("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})


@app.get("/accept-presentation-response/", tags=["Brand"])
def accept_presentation_response(brand_api_key: str = Header(None)):
    client.set_default_header('apiKey', brand_api_key)

    presentationApi = PresentProofApi(client)

    body = swagger_client.RequestPresentationAction(action="presentation-accept")

    try:
        res = presentationApi.update_presentation(body=body, presentation_id="4af6b5fb-b8f9-4197-96d2-6b155d5daa39")
        pprint(serialize(res))
        return JSONResponse(content=serialize(res), status_code=200)
    except ApiException as e:
        print("Exception when calling PresentProofApi->update_presentation: %s\n" % e)
        raise HTTPException(status_code=e.status, detail={"reason": e.reason})