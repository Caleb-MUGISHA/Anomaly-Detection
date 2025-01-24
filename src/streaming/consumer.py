from confluent_kafka import Consumer, KafkaException
import logging
from src.ml.anomaly_detector import AnomalyDetector
from src.database.consensus import DatabaseCluster

class TransactionConsumer:
    def __init__(self):
        self.conf = {
            'bootstrap.servers': ','.join(Config.KAFKA_BROKERS),
            'group.id': 'fraud-detection-group',
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False
        }
        self.consumer = Consumer(self.conf)
        self.detector = AnomalyDetector()
        self.db_cluster = DatabaseCluster(['primary', 'secondary'])

    def process_messages(self):
        self.consumer.subscribe([Config.TRANSACTIONS_TOPIC])
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                
                transaction = eval(msg.value().decode('utf-8'))
                
                if self.detector.is_anomalous(transaction):
                    transaction['is_fraud'] = 1
                else:
                    transaction['is_fraud'] = 0
                
                if self.db_cluster.write_transaction(transaction):
                    self.consumer.commit(msg)
                else:
                    logging.error("Failed to achieve quorum")
                    self.consumer.seek(msg.partition(), msg.offset())
        finally:
            self.consumer.close()

if __name__ == "__main__":
    TransactionConsumer().process_messages()
