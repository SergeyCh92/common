import logging
import ssl

from pika import BlockingConnection, ConnectionParameters, PlainCredentials, SSLOptions
from pika.adapters.blocking_connection import BlockingChannel

from .models import BaseRequest, CommonRequest
from .settings import RabbitSettings


class RabbitConnector:
    def __init__(self, settings: RabbitSettings):
        self.host: str = settings.host
        self.port: int = settings.port
        self.ca_cert_path: str = settings.ca_cert_path
        self.client_cert_path: str = settings.client_cert_path
        self.key_file_path: str = settings.client_key_path
        self.cert_password: str | None = settings.cert_password
        self.user: str = settings.user
        self.password: str = settings.password
        self.channel = self._get_channel()

    def _get_channel(self) -> BlockingChannel:
        ssl_options = None
        if self.port == 5671:
            context = ssl.create_default_context(cafile=self.ca_cert_path)
            context.verify_mode = ssl.CERT_REQUIRED
            context.load_cert_chain(self.client_cert_path, self.key_file_path, self.cert_password)
            ssl_options = SSLOptions(context, self.host)

        connection_params = ConnectionParameters(
            host=self.host,
            port=self.port,
            ssl_options=ssl_options,
            credentials=PlainCredentials(self.user, self.password),
        )

        connection = BlockingConnection(connection_params)
        return connection.channel()

    def _deserialize_data(self, data: bytes, data_type: type[CommonRequest]) -> BaseRequest | None:
        try:
            string_data = data.decode("utf-8")
            result = data_type.model_validate_json(string_data)
        except Exception as err:
            logging.error(f"failed to parse data {string_data}, error: {err}")
            result = None
        return result
