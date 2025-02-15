import logging
import hashlib
import logging
from datetime import datetime
from typing import List, Dict
from tabulate import tabulate

# Description: This file contains the implementation of the Ledger class.
# Ledger Class

class Ledger:
    def __init__(self, logger):
        self.transactions = []
        self.balances = {}
        self.logger = logger
        self.logger.info("Ledger Initialized...")

    def generate_hash(self, sender: str, receiver: str, amount: float, timestamp: str) -> str:
        """Generate SHA-256 hash for transactions."""
        data = f"{sender}{receiver}{amount}{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def record_transaction(self, sender: str, receiver: str, amount: float, is_credit: bool, description: str) -> str:
            """Internal function to add transactions while maintaining balance updates."""
            if amount <= 0:
                return "Amount must be greater than zero."

            timestamp = datetime.utcnow().isoformat()
            hash_value = self.generate_hash(sender, receiver, amount, timestamp)

            # Ensure the transaction is unique
            for txn in self.transactions:
                if txn["hash"] == hash_value:
                    logging.error("Duplicate transaction detected.")
                    return "Transaction already exists."

            credit_debit = "Credit" if is_credit == True else "debit"
            transaction = {
                "id": len(self.transactions) + 1,
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "timestamp": timestamp,
                "hash": hash_value,
                "transaction_type": credit_debit,
                "desription": description
            }
            
            self.transactions.append(transaction)

            # Update balances
            if is_credit is True:
                self.balances[receiver] = self.balances.get(receiver, 0) + amount
            else:
                self.balances[sender] = self.balances.get(sender, 0) - amount

            logging.info(f"Transaction recorded: {sender} -> {receiver}, Amount: {amount}, transaction type: {credit_debit}, Hash: {hash_value}")
            return "Transaction recorded successfully."           
    
    def deposit(self, user: str, receiver: str, amount: float, description: str) -> str:
        """Deposit money into a user's account."""
        return self.record_transaction(receiver, user, amount, True, description)

    def withdraw(self, user: str, receiver: str, amount: float, description: str) -> str:
        """Withdraw money from a user's account if balance allows."""
        if self.balances.get(user, 0) < amount:
            return "Insufficient funds."
        return self.record_transaction(user, receiver, amount, False, description)

    def get_balance(self, user: str) -> str:
        """Withdraw money from a user's account if balance allows."""
        balance = self.balances.get(user, 0)
        return f"Balance for {user}: {balance}"
    
    def transfer(self, sender: str, receiver: str, amount: float,  description: str) -> str:
        """Transfer money between users."""
        if self.balances.get(sender, 0) < amount:
            return "Insufficient funds."
        #first, withdraw the amount from the sender
        self.withdraw(sender, receiver, amount, description)
        self.deposit(receiver, sender, amount, description)
        return "Transfer successful."

    def get_transaction(self, transaction_hash: str) -> Dict:
        """Retrieve a transaction by its hash."""
        for txn in self.transactions:
            if txn["hash"] == transaction_hash:
                return txn
        return {}


    def get_transactions_history(self) -> List[Dict]:
        """Retrieve all transactions."""
        return self.transactions

    def get_tabulate_transactions(self):
        """Prints all transactions in a tabular format."""
        if not self.transactions:
            print("No transactions found.")
            return
        
        headers = ["ID", "Sender", "Receiver", "Amount", "Timestamp", "Hash"]
        table_data = [[txn["id"], txn["sender"], txn["receiver"], txn["amount"], txn["timestamp"], txn["hash"]] 
                    for txn in self.transactions]
        return tabulate(table_data, headers=headers, tablefmt="grid")

    def print_tabulate_transactions_history(self) -> List[Dict]:
        """Retrieve all transactions."""
        tab_transactions = self.get_tabulate_transactions()
        print(tab_transactions)
        return tab_transactions