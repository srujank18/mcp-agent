from praisonaiagents import Agent, MCP, PraisonAIAgents
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY in .env")

# Agents for each tool
crypto_agent = Agent(
    instructions="You are a helpful assistant. Use the crypto tool when price info is needed.",
    llm="groq/llama3-8b-8192",
    api_key=API_KEY,
    tools=MCP("python src/servers/crypto_prices.py")
)

news_agent = Agent(
    instructions="You are a helpful assistant. Use the daily news tool when news is requested.",
    llm="groq/llama3-8b-8192",
    api_key=API_KEY,
    tools=MCP("python src/servers/daily_news.py")
)

# Combine into multi-tool setup
multi_agents = PraisonAIAgents(agents=[crypto_agent, news_agent])

print("🔧 Groq multi-tool agent initialized. Type 'exit' to quit.")
print("----------------------------------------------------------")

# Interactive loop
while True:
    try:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        response = multi_agents.start(user_input)
        print(f"🤖 Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
