from binance.client import Client
from dotenv import load_dotenv
import os


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError(
                "Missing Binance API credentials"
            )

        self.client = Client(api_key, api_secret)

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

    def get_client(self):
        return self.client