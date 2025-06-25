# memory_agent.py
import os
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver 

checkpointer = InMemorySaver()

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAkd68RyV6OpZQpZsCROpAwMRCXAr2NvrQ"

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Define your agent
agent = create_react_agent(
    model="google_genai:gemini-2.0-flash",
    tools=[get_weather],
    prompt="You are a helpful assistant",
    checkpointer=checkpointer)

config = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config  
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]},
    config
)

print("SF Response:", sf_response)
print("NY Response:", ny_response)