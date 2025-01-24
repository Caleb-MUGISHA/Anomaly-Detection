from functools import wraps
from flask import request, jsonify
import jwt
from cryptography.fernet import Fernet

def encrypt_data(data: str) -> bytes:
    cipher = Fernet(Config.ENCRYPTION_KEY)
    return cipher.encrypt(data.encode())

def decrypt_data(token: bytes) -> str:
    cipher = Fernet(Config.ENCRYPTION_KEY)
    return cipher.decrypt(token).decode()

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Unauthorized"}), 401
        try:
            jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        except jwt.PyJWTError:
            return jsonify({"error": "Invalid token"}), 403
        return f(*args, **kwargs)
    return decorated
