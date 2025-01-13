from flask_restful import Resource
from flask import request
import requests

FUTURE_RPC_URL = "http://44.192.49.112:9696"
AUTH = ('dominic', '12345698')

class Transaction(Resource):
    def post(self):
        data = request.get_json()

        # Validate input
        required_fields = ["from", "to", "amount", "private_key"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return {"error": "Missing fields", "details": missing_fields}, 400

        try:
            response = requests.post(f"{FUTURE_RPC_URL}/transaction", json=data, auth=AUTH)
            response.raise_for_status()
            return response.json(), 200
        except requests.exceptions.RequestException as e:
            return {"error": "Transaction failed", "details": str(e)}, 500
