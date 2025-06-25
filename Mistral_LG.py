from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from langchain_mistralai import ChatMistralAI
import os

#api  key
os.environ["MISTRAL_API_KEY"] = "l1xd5hefUrdsjIAmhiIlLyVzeA0MtGKe"

#state def
class State(TypedDict):
    question: str
    answer: str

llm = ChatMistralAI(model="mistral-small", temperature=0)

#node to send the question request and store it's response
def ask_mistral(state:State):
    response = llm.predict(state["question"])
    return {"answer": response}

#building the graph
graph = StateGraph(State)
graph.add_node("ask_mistral", ask_mistral)
graph.set_entry_point("ask_mistral")
graph.add_edge("ask_mistral", END)
app = graph.compile()
result = app.invoke({"question": "Define Agentic AI?"})
print(result["answer"])


