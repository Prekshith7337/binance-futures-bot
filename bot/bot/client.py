from binance.client import Client
import os

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com"

    return client