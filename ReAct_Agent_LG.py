import os
#  Import the prebuilt ReAct‐style agent factory
#    This one function spins up a full Prompt → LLM → Tool graph for you.
from langgraph.prebuilt import create_react_agent 


# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAkd68RyV6OpZQpZsCROpAwMRCXAr2NvrQ"

# . Define your tool
# Define any “tools” as plain Python functions.
#    Here get_weather will be automatically wrapped into a ToolNode.
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

#  Create the ReAct agent using Gemini
#    - model=... tells LangGraph to instantiate the correct LLMNode (Gemini via Google GenAI)
#    - tools=[...] wires in our get_weather ToolNode
#    - prompt="…" becomes a system‐prompt PromptNode at the head of the graph
agent = create_react_agent(
    model="google_genai:gemini-2.0-flash", 
    tools=[get_weather],  # our custom tool(s)
    prompt="You are a helpful assistant" # system prompt for the LLM
)

#  Invoke the agent
#    - agent.invoke(...) serializes messages to text,
#      runs PromptNode → LLMNode → ToolRouterNode → ToolNode → back to LLMNode
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in delhi"}]}
)

print(response)
