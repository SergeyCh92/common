import json
import logging

from pika.exceptions import ChannelClosed

from .connector import RabbitConnector


class RabbitProducer(RabbitConnector):
    def send_message(self, data: str | dict, exchange: str, routing_key: str):
        bytes_data = (
            data.encode("utf-8") if isinstance(data, str) else json.dumps(data).encode("utf-8")
        )
        try:
            self.channel.queue_declare(routing_key, passive=True)
        except ChannelClosed:
            logging.error(f"there is no {routing_key} response queue in RabbitMQ")
        else:
            self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=bytes_data)
