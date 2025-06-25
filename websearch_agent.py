# websearch_agent.py
import os
import requests
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from duckduckgo_search import DDGS 
from tavily import TavilyClient
from langgraph.graph import StateGraph, START, END


os.environ["TAVILY_API_KEY"] = "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"
os.environ["GOOGLE_API_KEY"] = "AIzaSyAkd68RyV6OpZQpZsCROpAwMRCXAr2NvrQ"

def search_duckduckgo(query: str) -> str:
    
    """
    Uses DuckDuckGo to return the top 5 titles & snippets.
    """
    results = DDGS().text(query, max_results=5)
    lines = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "").strip()
        snippet = r.get("body", "").strip()
        lines.append(f"{i}. {title} — {snippet}")
    return "\n".join(lines)

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def search_tavily(query: str) -> str:
    """
    Uses the Tavily API to return a concise, AI-optimized answer.
    """
    response = tavily_client.search(query)
    # response is typically a dict with 'answer' and list of 'results'
    answer = response.get("answer") or "No concise answer returned."
    # Optionally include the top URLs:
    urls = [r.get("url") for r in response.get("results", [])[:3]]
    urls_text = "\n".join(f"- {u}" for u in urls if u)
    return f"Answer:\n{answer}\n\nSources:\n{urls_text}"

# checkpointer = InMemorySaver()

agent = create_react_agent(
    model="google_genai:gemini-2.0-flash",
    tools=[search_duckduckgo, search_tavily],
    prompt=(
        "You are a research assistant.  \n"
        "When you need up-to-date web info, choose the appropriate tool:\n"
        "- `search_duckduckgo(query)` for general, privacy-focused searches;\n"
        "- `search_tavily(query)` for AI-optimized, citation-ready summaries.\n"
        "Think step by step, and never hallucinate beyond tool outputs."
    ),
    # checkpointer=checkpointer,
)
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is langgraph?"}]},
)

# print("=== DuckDuckGo ===")
# print(search_duckduckgo("explain langgraph"))

# print("\n=== Tavily ===")
# print(search_tavily("explain langgraph"))

# print("\n=== Agent ===")
# print(response)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "what is langgraph?"}]},
    stream_mode="values"
):
    msg = chunk["messages"][-1]
    msg.pretty_print()
