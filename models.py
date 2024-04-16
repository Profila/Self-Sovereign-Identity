from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name: str

class CredentialOfferRequest(BaseModel):
    issuerDid: str
    connectionId: str
    email: str
    name: str
    surname: str
