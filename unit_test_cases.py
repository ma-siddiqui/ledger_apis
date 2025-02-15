import unittest
from ledger import Ledger
import logging

class TestLedger(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test_logger")
        self.ledger = Ledger(self.logger)

    def test_deposit(self):
        response = self.ledger.deposit("user1", "bank", 100, "Initial deposit")
        self.assertEqual(response, "Transaction recorded successfully.")
        self.assertEqual(self.ledger.get_balance("user1"), "Balance for user1: 100")

    def test_withdraw_success(self):
        self.ledger.deposit("user1", "bank", 200, "Deposit")
        response = self.ledger.withdraw("user1", "shop", 50, "Purchase")
        self.assertEqual(response, "Transaction recorded successfully.")
        self.assertEqual(self.ledger.get_balance("user1"), "Balance for user1: 150")
    
    def test_withdraw_insufficient_funds(self):
        response = self.ledger.withdraw("user1", "shop", 50, "Attempt overdraft")
        self.assertEqual(response, "Insufficient funds.")

    def test_transfer_success(self):
        self.ledger.deposit("user1", "bank", 300, "Deposit")
        response = self.ledger.transfer("user1", "user2", 100, "Payment")
        self.assertEqual(response, "Transfer successful.")
        self.assertEqual(self.ledger.get_balance("user1"), "Balance for user1: 200")
        self.assertEqual(self.ledger.get_balance("user2"), "Balance for user2: 100")

    def test_transfer_insufficient_funds(self):
        response = self.ledger.transfer("user1", "user2", 50, "Attempt transfer")
        self.assertEqual(response, "Insufficient funds.")

    def test_get_transaction_history(self):
        self.ledger.deposit("user1", "bank", 100, "Deposit")
        transactions = self.ledger.get_transactions_history()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["amount"], 100)

if __name__ == "__main__":
    unittest.main()
