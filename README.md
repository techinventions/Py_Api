# Py_Api

# Future Blockchain API

## Description
A RESTful API to interact with the Future blockchain, enabling developers to:
- Retrieve gas fees.
- Check balances.
- Initiate transactions.

## Endpoints
### 1. `/api/gas-fee` (GET)
- Fetches the current gas fee.

### 2. `/api/balance/<address>` (GET)
- Retrieves the balance of a given address.
- **Input**: Address (e.g., `0xabc123...`).

### 3. `/api/transaction` (POST)
- Initiates a blockchain transaction.
- **Input** (JSON):
  - `from`: Sender's address.
  - `to`: Receiver's address.
  - `amount`: Amount to transfer.
  - `private_key`: Private key for the sender's wallet.

### 4. `/api/health` (GET)
- Checks API status.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
