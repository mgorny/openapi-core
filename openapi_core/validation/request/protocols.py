"""OpenAPI core validation request protocols module"""

from typing import Iterator
from typing import Optional
from typing import Protocol
from typing import runtime_checkable

from jsonschema_path import SchemaPath
from openapi_spec_validator.validation.types import SpecValidatorType

from openapi_core.casting.schemas.factories import SchemaCastersFactory
from openapi_core.deserializing.media_types import (
    media_type_deserializers_factory,
)
from openapi_core.deserializing.media_types.datatypes import (
    MediaTypeDeserializersDict,
)
from openapi_core.deserializing.media_types.factories import (
    MediaTypeDeserializersFactory,
)
from openapi_core.deserializing.styles import style_deserializers_factory
from openapi_core.deserializing.styles.factories import (
    StyleDeserializersFactory,
)
from openapi_core.protocols import Request
from openapi_core.protocols import WebhookRequest
from openapi_core.security import security_provider_factory
from openapi_core.security.factories import SecurityProviderFactory
from openapi_core.validation.schemas.datatypes import FormatValidatorsDict
from openapi_core.validation.schemas.factories import SchemaValidatorsFactory


@runtime_checkable
class RequestValidator(Protocol):
    def __init__(
        self,
        spec: SchemaPath,
        base_url: Optional[str] = None,
        style_deserializers_factory: StyleDeserializersFactory = style_deserializers_factory,
        media_type_deserializers_factory: MediaTypeDeserializersFactory = media_type_deserializers_factory,
        schema_casters_factory: Optional[SchemaCastersFactory] = None,
        schema_validators_factory: Optional[SchemaValidatorsFactory] = None,
        spec_validator_cls: Optional[SpecValidatorType] = None,
        format_validators: Optional[FormatValidatorsDict] = None,
        extra_format_validators: Optional[FormatValidatorsDict] = None,
        extra_media_type_deserializers: Optional[
            MediaTypeDeserializersDict
        ] = None,
        security_provider_factory: SecurityProviderFactory = security_provider_factory,
    ): ...

    def iter_errors(
        self,
        request: Request,
    ) -> Iterator[Exception]: ...

    def validate(
        self,
        request: Request,
    ) -> None: ...


@runtime_checkable
class WebhookRequestValidator(Protocol):
    def __init__(
        self,
        spec: SchemaPath,
        base_url: Optional[str] = None,
        style_deserializers_factory: StyleDeserializersFactory = style_deserializers_factory,
        media_type_deserializers_factory: MediaTypeDeserializersFactory = media_type_deserializers_factory,
        schema_casters_factory: Optional[SchemaCastersFactory] = None,
        schema_validators_factory: Optional[SchemaValidatorsFactory] = None,
        spec_validator_cls: Optional[SpecValidatorType] = None,
        format_validators: Optional[FormatValidatorsDict] = None,
        extra_format_validators: Optional[FormatValidatorsDict] = None,
        extra_media_type_deserializers: Optional[
            MediaTypeDeserializersDict
        ] = None,
        security_provider_factory: SecurityProviderFactory = security_provider_factory,
    ): ...

    def iter_errors(
        self,
        request: WebhookRequest,
    ) -> Iterator[Exception]: ...

    def validate(
        self,
        request: WebhookRequest,
    ) -> None: ...
