# coding: utf-8

# flake8: noqa

"""
    Open Enterprise Agent API Reference

     The Open Enterprise Agent API facilitates the integration and management of self-sovereign identity capabilities within applications. It supports DID (Decentralized Identifiers) management, verifiable credential exchange, and secure messaging based on DIDComm standards. The API is designed to be interoperable with various blockchain and DLT (Distributed Ledger Technology) platforms, ensuring wide compatibility and flexibility. Key features include connection management, credential issuance and verification, and secure, privacy-preserving communication between entities. Additional information and the full list of capabilities can be found in the [Open Enterprise Agent documentation](https://docs.atalaprism.io/docs/category/prism-cloud-agent)   # noqa: E501

    OpenAPI spec version: 1.31.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.connections_management_api import ConnectionsManagementApi
from swagger_client.api.credential_definition_registry_api import CredentialDefinitionRegistryApi
from swagger_client.api.credential_status_list_api import CredentialStatusListApi
from swagger_client.api.did_api import DIDApi
from swagger_client.api.did_registrar_api import DIDRegistrarApi
from swagger_client.api.events_api import EventsApi
from swagger_client.api.identity_and_access_management_api import IdentityAndAccessManagementApi
from swagger_client.api.issue_credentials_protocol_api import IssueCredentialsProtocolApi
from swagger_client.api.present_proof_api import PresentProofApi
from swagger_client.api.schema_registry_api import SchemaRegistryApi
from swagger_client.api.system_api import SystemApi
from swagger_client.api.verification_api import VerificationApi
from swagger_client.api.wallet_management_api import WalletManagementApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.accept_connection_invitation_request import AcceptConnectionInvitationRequest
from swagger_client.models.accept_credential_offer_request import AcceptCredentialOfferRequest
from swagger_client.models.action_type import ActionType
from swagger_client.models.anoncred_credential_proof_v1 import AnoncredCredentialProofV1
from swagger_client.models.anoncred_credential_proofs_v1 import AnoncredCredentialProofsV1
from swagger_client.models.anoncred_non_revoked_interval_v1 import AnoncredNonRevokedIntervalV1
from swagger_client.models.anoncred_presentation_request_v1 import AnoncredPresentationRequestV1
from swagger_client.models.anoncred_requested_attribute_v1 import AnoncredRequestedAttributeV1
from swagger_client.models.anoncred_requested_predicate_v1 import AnoncredRequestedPredicateV1
from swagger_client.models.api_key_authentication_request import ApiKeyAuthenticationRequest
from swagger_client.models.arr import Arr
from swagger_client.models.bool import Bool
from swagger_client.models.connection import Connection
from swagger_client.models.connection_invitation import ConnectionInvitation
from swagger_client.models.connections_page import ConnectionsPage
from swagger_client.models.create_connection_request import CreateConnectionRequest
from swagger_client.models.create_entity_request import CreateEntityRequest
from swagger_client.models.create_issue_credential_record_request import CreateIssueCredentialRecordRequest
from swagger_client.models.create_managed_did_response import CreateManagedDIDResponse
from swagger_client.models.create_managed_did_request import CreateManagedDidRequest
from swagger_client.models.create_managed_did_request_document_template import CreateManagedDidRequestDocumentTemplate
from swagger_client.models.create_wallet_request import CreateWalletRequest
from swagger_client.models.create_wallet_uma_permission_request import CreateWalletUmaPermissionRequest
from swagger_client.models.create_webhook_notification import CreateWebhookNotification
from swagger_client.models.credential_definition_input import CredentialDefinitionInput
from swagger_client.models.credential_definition_response import CredentialDefinitionResponse
from swagger_client.models.credential_definition_response_page import CredentialDefinitionResponsePage
from swagger_client.models.credential_schema_input import CredentialSchemaInput
from swagger_client.models.credential_schema_response import CredentialSchemaResponse
from swagger_client.models.credential_schema_response_page import CredentialSchemaResponsePage
from swagger_client.models.credential_subject import CredentialSubject
from swagger_client.models.did_document import DIDDocument
from swagger_client.models.did_document_metadata import DIDDocumentMetadata
from swagger_client.models.did_operation_response import DIDOperationResponse
from swagger_client.models.did_resolution_metadata import DIDResolutionMetadata
from swagger_client.models.did_resolution_result import DIDResolutionResult
from swagger_client.models.did_operation_submission import DidOperationSubmission
from swagger_client.models.entity_response import EntityResponse
from swagger_client.models.entity_response_page import EntityResponsePage
from swagger_client.models.error_response import ErrorResponse
from swagger_client.models.health_info import HealthInfo
from swagger_client.models.issue_credential_record import IssueCredentialRecord
from swagger_client.models.issue_credential_record_page import IssueCredentialRecordPage
from swagger_client.models.json import Json
from swagger_client.models.managed_did import ManagedDID
from swagger_client.models.managed_did_key_template import ManagedDIDKeyTemplate
from swagger_client.models.managed_did_page import ManagedDIDPage
from swagger_client.models.map_anoncred_requested_attribute_v1 import MapAnoncredRequestedAttributeV1
from swagger_client.models.map_anoncred_requested_predicate_v1 import MapAnoncredRequestedPredicateV1
from swagger_client.models.map_string import MapString
from swagger_client.models.model_str import ModelStr
from swagger_client.models.null import Null
from swagger_client.models.num import Num
from swagger_client.models.obj import Obj
from swagger_client.models.one_of_service_type import OneOfServiceType
from swagger_client.models.one_of_update_managed_did_service_action_type import OneOfUpdateManagedDIDServiceActionType
from swagger_client.models.options import Options
from swagger_client.models.patch_context_action import PatchContextAction
from swagger_client.models.presentation_status import PresentationStatus
from swagger_client.models.presentation_status_page import PresentationStatusPage
from swagger_client.models.proof import Proof
from swagger_client.models.proof1 import Proof1
from swagger_client.models.proof_request_aux import ProofRequestAux
from swagger_client.models.public_key_jwk import PublicKeyJwk
from swagger_client.models.purpose import Purpose
from swagger_client.models.remove_entry_by_id import RemoveEntryById
from swagger_client.models.request_presentation_action import RequestPresentationAction
from swagger_client.models.request_presentation_input import RequestPresentationInput
from swagger_client.models.revocation import Revocation
from swagger_client.models.service import Service
from swagger_client.models.status_list_credential import StatusListCredential
from swagger_client.models.status_purpose import StatusPurpose
from swagger_client.models.suspension import Suspension
from swagger_client.models.update_entity_name_request import UpdateEntityNameRequest
from swagger_client.models.update_entity_wallet_id_request import UpdateEntityWalletIdRequest
from swagger_client.models.update_managed_did_request import UpdateManagedDIDRequest
from swagger_client.models.update_managed_did_request_action import UpdateManagedDIDRequestAction
from swagger_client.models.update_managed_did_service_action import UpdateManagedDIDServiceAction
from swagger_client.models.verification_method import VerificationMethod
from swagger_client.models.verification_policy_constraint import VerificationPolicyConstraint
from swagger_client.models.verification_policy_input import VerificationPolicyInput
from swagger_client.models.verification_policy_response import VerificationPolicyResponse
from swagger_client.models.verification_policy_response_page import VerificationPolicyResponsePage
from swagger_client.models.wallet_detail import WalletDetail
from swagger_client.models.wallet_detail_page import WalletDetailPage
from swagger_client.models.webhook_notification import WebhookNotification
from swagger_client.models.webhook_notification_page import WebhookNotificationPage
