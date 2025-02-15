from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import time

# Request Models
class TransactionRequest(BaseModel):
    sender: str
    receiver: str
    amount: float
    description: str

# API Class
class LedgerAPIServer:
    def __init__(self, host, port, ledger_instance, logger):
        self.app = FastAPI()
        self.ledger = ledger_instance
        self.host = host
        self.port = port
        self.logger = logger
        self.setup_routes()

    def run_api_server(self):
        self.logger.info(f"Starting API Server at {self.host}:{self.port}")
        uvicorn.run(app = self.app, host = self.host, port = self.port)
        self.logger.info("API Server Stopped...")

    def setup_routes(self):
        @self.app.post("/transaction/deposit/")
        def deposit(request: TransactionRequest):
            try:
                self.logger.info(f"Received Transaction (deposit) Request: {request}")
                return self.ledger.deposit(request.sender, request.receiver, request.amount, request.description)
            except ValueError as e:
                self.logger.error(f"Error: {e}")
                raise HTTPException(status_code=400, detail=str(e))
        @self.app.post("/transaction/withdraw/")
        def withdraw(request: TransactionRequest):
            try:
                self.logger.info(f"Received Transaction (withdraw) Request: {request}")
                return self.ledger.withdraw(request.sender, request.receiver, request.amount, request.description)
            except ValueError as e:
                self.logger.error(f"Error: {e}")
                raise HTTPException(status_code=400, detail=str(e))
        
        
        @self.app.post("/transaction/transfer/")
        def deposit(request: TransactionRequest):
            try:
                self.logger.info(f"Received Transaction (transfer) Request: {request}")
                return self.ledger.transfer(request.sender, request.receiver, request.amount, request.description)
            except ValueError as e:
                self.logger.error(f"Error: {e}")
                raise HTTPException(status_code=400, detail=str(e))
            
        @self.app.get("/transaction/balance/")
        def get_balance(user: str):
            self.logger.info("Received Balance Request")
            return self.ledger.get_balance(user)

        @self.app.get("/transaction/history/")
        def get_transactions_history():
            self.logger.info("Received Transaction History Request")
            return self.ledger.get_transactions_history()

        @self.app.get("/transaction/tabular/history/")
        def get_transactions_history_tabular():
            self.logger.info("Received Transaction History Request")
            return self.ledger.get_tabulate_transactions()
        
        @self.app.get("/transaction/print/tabular/history/")
        def print_transactions_history_tabular():
            self.logger.info("Received Transaction History Request")
            return self.ledger.print_tabulate_transactions_history()