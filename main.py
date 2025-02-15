import logging
from ledger_api_server import LedgerAPIServer
from ledger import Ledger

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_ledger_server(host="0.0.0.0", port=8000):
    ledger = Ledger(logger)
    logger.info("Starting Ledger Server...")
    ledger_api_server = LedgerAPIServer(host, port, ledger, logger)
    ledger_api_server.run_api_server()
    logger.info("Exiting Ledger Server...")

if __name__ == "__main__":
    run_ledger_server()
   