from pydantic import BaseModel, Field
from typing import List

class CreateEntityRequest(BaseModel):
    name: str

class Claim(BaseModel):
    name: str = Field(..., example="email")
    value: str = Field(..., example="alice@gmail.com")

class CredentialOfferRequest(BaseModel):
    issuerDid: str = Field(..., example="did:example:123456789abcdefghi")
    connectionId: str = Field(..., example="123456789abcdefghi")
    attrClaims : list[Claim] 

class Attribute(BaseModel):
    name: str = Field(..., example="email")
    dataType: str = Field(..., example="string")

class CreateSchemaRequest(BaseModel):
    schemaName: str = Field(..., example="Test_Profile_2")
    schemaVersion: str = Field(..., example="1.0.0")
    schemaDescription: str = Field(..., example="This is a test schema")
    schemaId: str = Field(..., example="https://profila.com/profila-profile-1.0.0")
    schemaTags: List[str] = Field(..., example=["test"])
    attributes: List[Attribute] = Field(...)