from flask import Flask
from flask_restful import Api
from api.gas_fee import GasFee
from api.balance import Balance
from api.transaction import Transaction
from api.health import Health

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(GasFee, '/api/gas-fee')
api.add_resource(Balance, '/api/balance/<string:address>')
api.add_resource(Transaction, '/api/transaction')
api.add_resource(Health, '/api/health')

# Root route
@app.route('/')
def index():
    return {
        "message": "Welcome to the Future Blockchain API",
        "endpoints": {
            "Gas Fee": "/api/gas-fee",
            "Balance": "/api/balance/<address>",
            "Transaction": "/api/transaction",
            "Health": "/api/health"
        }
    }, 200

# Favicon route
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
