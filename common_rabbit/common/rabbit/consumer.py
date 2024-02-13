from .connector import RabbitConnector
from .models import BaseRequest, CommonRequest
from .settings import RabbitSettings


class RabbitConsumer(RabbitConnector):
    def __init__(self, settings: RabbitSettings):
        super().__init__(settings)

    def receive(self, data_type: type[CommonRequest]) -> BaseRequest | None:
        method_frame, header_frame, body = self.channel.basic_get("", auto_ack=True)
        if body is None:
            result = None
        else:
            result = self._deserialize_data(body, data_type)
        return result
