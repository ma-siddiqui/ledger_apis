# Ledger API Server

This project provides a simple ledger system for recording and managing transactions using a Python-based API server.

## Features
- Record transactions (credit/debit)
- Track balances for users
- Retrieve transaction history
- Expose APIs via `LedgerAPIServer`

## Requirements
- Python 3.9+
- `pip` package manager

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ledger-api.git
   cd ledger-api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the server:
   ```sh
   python server.py
   ```

## Running with Docker

1. Build the Docker image:
   ```sh
   docker build -t ledger-api .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 ledger-api
   ```

## API Endpoints

- **POST /deposit** - Deposit money into an account
- **POST /withdraw** - Withdraw money from an account
- **POST /transfer** - Transfer money between accounts
- **GET /balance/{user}** - Get the balance for a user
- **GET /transactions** - Retrieve all transactions

## Logging
Logs are generated using Python's `logging` module and can be viewed in the console or redirected to a file.

# Results and transaction history (Example)

+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|   ID | Sender   | Receiver   |   Amount | Timestamp                  | Hash                                                             |
+======+==========+============+==========+============================+==================================================================+
|    1 | bank     | ajmal      |     1000 | 2025-02-15T15:37:51.305641 | d92c760abf713a300b2f4b34a8e631fda8e9948aaa026b07430e3e9b8fe0983b |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    2 | bank     | ajmal      |     1000 | 2025-02-15T15:37:56.252862 | 959c974b00d23d824b4e6d5c6dd66800b8d65837091faa003781105d8ce9bacf |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    3 | bank     | ajmal      |     1000 | 2025-02-15T15:37:57.128189 | 564807018814aab2eb22ac9e6dffc52d282fa3706432a5dc70a4d85f3db9e631 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    4 | bank     | ajmal      |     1000 | 2025-02-15T15:37:57.777923 | 82a800e3963e90bb158b39534bba1fd74467141e48bb3b4287bb2a4e8feb652e |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    5 | bank     | ajmal      |     1000 | 2025-02-15T15:37:58.398254 | c80377a45e356c9fb2a7f7bd466b29f8141cda08a1ec46e7e775ad7c0066a7a8 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    6 | bank     | ajmal      |     1000 | 2025-02-15T15:37:58.963567 | dd946ace0b8d8dfb7d86e9585b0bedd1b9e6b03cbf617da7076975451f005412 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    7 | bank     | ajmal      |     1000 | 2025-02-15T15:37:59.478370 | 9f14efe163b0efaffb93bb6af2952357af4be50b22ecaece6b77326e7a93a706 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    8 | bank     | ajmal      |     1000 | 2025-02-15T15:38:00.001847 | ffa61212d61513a91b43acd22b994f55870b80121e960140e340645319e21e79 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
|    9 | bank     | ajmal      |     1000 | 2025-02-15T15:38:00.568445 | d69a5950f1899c2305c832395b3cd1f49220fee670de458a21e4e41c8c5dea37 |
+------+----------+------------+----------+----------------------------+------------------------------------------------------------------+
