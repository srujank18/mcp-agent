from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
import signal
import sys

mcp = FastMCP(name="stock-news-agent", host="127.0.0.1", port=5000, timeout=30)


def signal_handler(sig, frame):
    print("Shutting down...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@mcp.tool()
def get_stock_news(ticker: str) -> str:
    """
    This function scrapes the latest news headlines (up to 5) from the Finviz stock quote page
    and returns them in a human-readable format, each with a timestamp, headline, and URL.

    Parameters:
        ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple Inc.).

    Returns:
        str: A newline-separated string of the latest headlines in the format:
             "Timestamp - Headline (URL)".
             If an error occurs during the scraping process, returns an error message.

    Raises:
        This function handles its own exceptions and returns an error message as a string
        instead of propagating exceptions.

    Example:
        >>> get_stock_news("GOOGL")
    """
    try:
        url = f"https://finviz.com/quote.ashx?t={ticker}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        news_table = soup.find('table', class_='fullview-news-outer')
        rows = news_table.find_all('tr')

        news = []
        for row in rows[:5]:  # Only grab latest 5 headlines
            time_tag = row.td.text.strip()
            headline = row.a.text.strip()
            link = row.a['href']
            news.append(f"{time_tag} - {headline} ({link})")

        return "\n".join(news)

    except Exception as e:
        return f"Error fetching news: {e}"


if __name__ == "__main__":
    print("Starting stock-news MCP server at PORT 5000...")
    mcp.run()