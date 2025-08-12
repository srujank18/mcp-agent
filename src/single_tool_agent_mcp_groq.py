from praisonaiagents import Agent, MCP
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY in .env")

# Create single-tool agent with Groq LLM
single_tool_agent = Agent(
    instructions="You are a helpful assistant. Call the crypto price tool when needed.",
    llm="groq/llama3-8b-8192",  # Example Groq model
    api_key=API_KEY,
    tools=MCP("python src/servers/crypto_prices.py")
)

print("🔧 Groq-powered agent initialized. Type 'exit' to quit.")
print("------------------------------------------------------")

# Interactive loop
while True:
    try:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting chat.")
            break
        response = single_tool_agent.start(user_input)
        print(f"🤖 Agent: {response}\n")
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting chat.")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
