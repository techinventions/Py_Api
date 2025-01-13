from flask_restful import Resource
from flask import jsonify
import requests
import re

FUTURE_RPC_URL = "http://44.192.49.112:9696"
AUTH = ('dominic', '12345698')

def validate_address(address):
    return re.match(r"^0x[a-fA-F0-9]{40}$", address)

class Balance(Resource):
    def get(self, address):
        if not validate_address(address):
            return {"error": "Invalid address format"}, 400

        try:
            response = requests.get(f"{FUTURE_RPC_URL}/balance/{address}", auth=AUTH)
            response.raise_for_status()
            return response.json(), 200
        except requests.exceptions.RequestException as e:
            return {"error": "Failed to fetch balance", "details": str(e)}, 500
