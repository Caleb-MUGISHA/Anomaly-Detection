from confluent_kafka import Producer
import logging
from config.settings import Config

class KafkaProducer:
    def __init__(self):
        self.conf = {
            'bootstrap.servers': Config.KAFKA_BROKERS[0],
            'message.max.bytes': 15728640,
            'queue.buffering.max.messages': 100000
        }
        self.producer = Producer(self.conf)

    def delivery_report(self, err, msg):
        if err:
            logging.error(f"Message delivery failed: {err}")
        else:
            logging.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def produce_transaction(self, transaction):
        self.producer.produce(
            Config.TRANSACTIONS_TOPIC,
            value=str(transaction).encode('utf-8'),
            callback=self.delivery_report
        )
        self.producer.poll(0)
