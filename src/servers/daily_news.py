from mcp.server.fastmcp import FastMCP
import signal
import sys
import requests
from bs4 import BeautifulSoup

# Initialize MCP
mcp = FastMCP(name="news-reader", host="127.0.0.1", port=8080, timeout=30)

# Graceful shutdown


def signal_handler(sig, frame):
    print("Shutting down...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@mcp.tool()
def get_latest_news(source: str = "npr") -> str:
    """
    Fetches the latest news headlines from a supported static news source.

    This tool currently supports the following sources:
    - 'npr'     → National Public Radio
    - 'bbc'     → BBC News
    Args:
        source (str): The news source to fetch headlines from. Must be one of:
                    'npr', 'bbc', or 'reuters'. Case-insensitive.

    Returns:
        str: A plain text string with the top 10 headlines from the selected source,
            separated by newlines. If the source is unsupported or an error occurs,
            a corresponding message is returned.

    Example:
        >>> get_latest_news("bbc")
    """
    try:
        source = source.lower()
        headlines = []

        if source == "npr":
            url = "https://www.npr.org/sections/news/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            articles = soup.find_all('h2', class_='title')[:10]
            headlines = [a.get_text(strip=True) for a in articles]

        elif source == "bbc":
            url = "https://www.bbc.com/news"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            articles = soup.select("h2")[:10]
            headlines = [a.get_text(strip=True) for a in articles]
        else:
            return "Unsupported news source."

        return "\n".join([f"- {h}" for h in headlines])

    except Exception as e:
        return f"Error while fetching news: {e}"


if __name__ == "__main__":
    print("Starting daily-news MCP server at PORT 8080...")
    mcp.run()