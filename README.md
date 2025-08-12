# mcp-agent
An AI-powered **Model Context Protocol (MCP)** agent that uses **Groq LLMs** to fetch **real-time world news, stock market updates, cryptocurrency prices, and Wikipedia summaries** — all through custom MCP servers and tools.



##  Features

- **Custom MCP Servers** — Easily extendable with your own Python tools.
- **Groq LLM Integration** — Fast and efficient inference using the Groq API.
- **Multiple Tools** — News, stock, crypto, and Wikipedia tools.
- **Single Tool Mode** — For lightweight use cases.
- **Environment Config** — Secure API key handling via `.env` file.

---

## 📂 Project Structure

```

mcp-agent/
├── src/
│   ├── servers/
│   │   ├── daily\_news.py          # Tool for real-time daily news
│   │   ├── stock\_news.py          # Tool for stock market news
│   │   ├── crypto\_prices.py       # Tool for crypto price updates
│   │   └── wikipedia\_summary.py   # Tool for Wikipedia summaries
│   ├── single\_tool\_agent\_mcp\_groq.py   # Runs single tool MCP agent
│   └── multi\_tool\_agent\_mcp\_groq.py    # Runs multiple tools MCP agent
├── multiple\_tools.json             # Config for multiple MCP servers
├── single\_tools.json               # Config for single MCP server
├── requirements.txt                # Python dependencies
├── .gitignore                      # Ignore sensitive and build files
└── README.md                       # Project documentation

````

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/<your-username>/mcp-agent.git
cd mcp-agent
````

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add your Groq API key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

*(The `.env` file is ignored by Git for security.)*

---

## Usage

### Run Single Tool Agent

```bash
python src/single_tool_agent_mcp_groq.py
```

### Run Multi Tool Agent

```bash
python src/multi_tool_agent_mcp_groq.py
```

---

## ⚙️ Configuration

MCP server configurations are stored in JSON files:

**Example — `multiple_tools.json`**

```json
{
  "mcpServers": {
    "stock-news": {
      "command": "python",
      "args": ["src/servers/stock_news.py"],
      "host": "127.0.0.1",
      "port": 5000,
      "timeout": 30000
    },
    "daily-news": {
      "command": "python",
      "args": ["src/servers/daily_news.py"],
      "host": "127.0.0.1",
      "port": 8080,
      "timeout": 30000
    }
  }
}
```

---

## Creating Your Own Tool

1. Create a new Python file inside `src/servers/`.
2. Define your MCP tool logic.
3. Add it to your JSON configuration file.
4. Run the agent and start using it immediately.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Pull requests are welcome!
If you’d like to add new tools or improve the agent, please fork the repo and submit a PR.

---

## 🌟 Acknowledgements

* [Model Context Protocol (MCP)](https://modelcontextprotocol.io)
* [Groq LLM API](https://groq.com)
* [Praison AI Agents](https://pypi.org/project/praisonaiagents/)

