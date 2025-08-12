from mcp.server.fastmcp import FastMCP
import requests
import signal
import sys

mcp = FastMCP(name="wikipedia-summary-agent",
              host="127.0.0.1", port=5050, timeout=30)


def signal_handler(sig, frame):
    print("Shutting down Wikipedia Summary Agent...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@mcp.tool()
def get_wikipedia_summary(topic: str) -> str:
    """
    Fetches the first paragraph summary of a given topic from Wikipedia.

    Parameters:
        topic (str): The topic to search for (e.g., "machine learning").

    Returns:
        str: The summary paragraph from the topic's Wikipedia page,
             or an error message if not found.

    Example:
        >>> get_wikipedia_summary("Python (programming language)")
    """
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        headers = {'User-Agent': 'WikiSummaryAgent/1.0'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary available.")
        elif response.status_code == 404:
            return "Topic not found on Wikipedia."
        else:
            return f"Unexpected response from Wikipedia: {response.status_code}"
    except Exception as e:
        return f"Error fetching summary: {e}"


if __name__ == "__main__":
    print("Starting Wikipedia Summary MCP server on PORT 5050...")
    mcp.run()