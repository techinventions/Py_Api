import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/api"

class TestAPI(unittest.TestCase):
    def test_health(self):
        response = requests.get(f"{BASE_URL}/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json())

    def test_gas_fee(self):
        response = requests.get(f"{BASE_URL}/gas-fee")
        self.assertEqual(response.status_code, 200)

    def test_balance(self):
        valid_address = "0xabc123abc123abc123abc123abc123abc123abc1"
        invalid_address = "invalid_address"

        # Test valid address
        response = requests.get(f"{BASE_URL}/balance/{valid_address}")
        self.assertEqual(response.status_code, 200)

        # Test invalid address
        response = requests.get(f"{BASE_URL}/balance/{invalid_address}")
        self.assertEqual(response.status_code, 400)

    def test_transaction(self):
        payload = {
            "from": "0xabc123abc123abc123abc123abc123abc123abc1",
            "to": "0xdef456def456def456def456def456def456def4",
            "amount": 10,
            "private_key": "private_key_here"
        }
        response = requests.post(f"{BASE_URL}/transaction", json=payload)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
