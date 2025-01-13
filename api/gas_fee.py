from flask_restful import Resource
import requests

FUTURE_RPC_URL = "http://44.192.49.112:9696"
AUTH = ('dominic', '12345698')

class GasFee(Resource):
    def get(self):
        try:
            response = requests.get(f"{FUTURE_RPC_URL}/gas-fee", auth=AUTH)
            response.raise_for_status()
            return response.json(), 200
        except requests.exceptions.RequestException as e:
            return {"error": "Failed to fetch gas fee", "details": str(e)}, 500
