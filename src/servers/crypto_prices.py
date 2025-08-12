from mcp.server.fastmcp import FastMCP
import requests
import signal
import sys

# Initialize MCP server
mcp = FastMCP(name="crypto-prices", host="127.0.0.1", port=6060, timeout=30)

# Graceful shutdown
def signal_handler(sig, frame):
    print("Shutting down Crypto Prices MCP server...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

@mcp.tool()
def get_crypto_price(symbol: str = "BTC") -> str:
    """
    Fetch the latest price for a cryptocurrency symbol from the CoinGecko API.

    Args:
        symbol (str): Cryptocurrency symbol (e.g., "BTC", "ETH", "DOGE").

    Returns:
        str: A human-readable string with the latest price in USD.
    """
    try:
        symbol = symbol.lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        response = requests.get(url)

        if response.status_code != 200:
            return f"Error: CoinGecko API returned {response.status_code}"

        data = response.json()
        if symbol not in data:
            return f"Symbol '{symbol.upper()}' not found."

        price = data[symbol]["usd"]
        return f"The current price of {symbol.upper()} is ${price} USD."

    except Exception as e:
        return f"Error fetching price: {e}"

if __name__ == "__main__":
    print("🚀 Starting Crypto Prices MCP server on PORT 6060...")
    mcp.run()
