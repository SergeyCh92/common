from common.rabbit.consumer import RabbitConsumer
from common.rabbit.models import CommonRequest
from common.rabbit.producer import RabbitProducer
from common.rabbit.settings import RabbitSettings


class MessageHandler:
    def __init__(self):
        self.rabbit_settings = RabbitSettings()
        self.consumer = RabbitConsumer(self.rabbit_settings)
        self.producer = RabbitProducer(self.rabbit_settings)

    def start(self, queue: str, data_type: type[CommonRequest]):
        self.consumer.channel.queue_declare(queue=queue, passive=True)

        while True:
            data = self.consumer.receive(data_type)
            if data:
                self._process_message(data)

    async def async_start(self, queue: str, data_type: type[CommonRequest]):
        self.consumer.channel.queue_declare(queue=queue, passive=True)

        while True:
            data = self.consumer.receive(data_type)
            if data:
                await self._process_message(data)
