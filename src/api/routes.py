from flask import Blueprint, request, jsonify
from src.utils.security import encrypt_data, jwt_required
from src.streaming.producer import KafkaProducer

api = Blueprint('api', __name__)
producer = KafkaProducer()

@api.route('/transactions', methods=['POST'])
@jwt_required
def create_transaction():
    data = request.get_json()
    producer.produce_transaction(data)
    return jsonify({"status": "processing"}), 202

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
