from pydantic import Field
from pydantic_settings import BaseSettings


class RabbitSettings(BaseSettings):
    host: str = Field(validation_alias="RABBIT_HOST", default="")
    # 5671 используется для TLS соединения, 5672 для TCP
    port: int = Field(validation_alias="RABBIT_PORT", default=5671)
    user: str = Field(validation_alias='RABBIT_USER', default="")
    password: str = Field(validation_alias="RABBIT_PASSWORD", default="")
    ca_cert_path: str = Field(validation_alias="RABBIT_CA_CERT_PATH", default="")
    client_cert_path: str = Field(validation_alias="RABBIT_CLIENT_CERT_PATH", default="")
    client_key_path: str = Field(validation_alias="RABBIT_CLIENT_KEY_PATH", default="")
    cert_password: str | None = Field(validation_alias="RABBIT_CERT_PASSWORD", default=None)
