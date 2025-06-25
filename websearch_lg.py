#websearch_lg.py

import sys
print("Python in use:", sys.executable)

#using DuckDuckGo - FREEE
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
#websearch and ai api imports
from mistralai import Mistral
# from mistralai.models.chat_completion import ChatMessage
from duckduckgo_search import DDGS 
import os

#setting up the api
os.environ["MISTRAL_API_KEY"] = "l1xd5hefUrdsjIAmhiIlLyVzeA0MtGKe"
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
model = "mistral-small" 

#state def
class State(TypedDict):
    question: str
    web_res: str
    answer: str

#node to web search
def web_search(state: State) -> State:
    query = state["question"]
    result = []
    with DDGS() as ddgs:  #DDGS() is the search engine wrapper
        for r in ddgs.text(query, max_results=5):  #performs the web search and returns results.
            result.append(f"{r['title']}: {r['body']}") #for each, extract title and body -> combine them into a string anser and rturn it to result 
    return {"web_res": "\n".join(result)} #the returned result from previous line is then assigned to our web_res KEY


#node for passing to mistral - asking the question and getting a breof ans
def ask_mistral(state: State) -> State:
    # messages = [
    #     {"role": "system", "content": "You are a helpful assistant who uses web search results to answer questions."},
    #     {"role": "user", "content": f"Question: {state['question']}\n\nWeb results:\n{state['web_results']}"}
    # ]#guide
    # response = client.chat(model="mistral-small", messages=messages)
    response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the latest features of LangGraph?"}
    ])
    print(response.choices[0].message.content)
    return {"answer": response.choices[0].message.content}

#building the grapg
graph = StateGraph(State)

graph.add_node("web_search", web_search)
graph.add_node("ask_mistral", ask_mistral)

graph.set_entry_point("web_search")
graph.add_edge("web_search","ask_mistral")
graph.add_edge("ask_mistral", END)

app = graph.compile()
question = "What are the latest features of LangGraph?"
result = app.invoke({"question": question})

print("\n Web Results:\n", result["web_res"])
print("\n Answer:\n", result["answer"])