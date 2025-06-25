#imports 
from langgraph.graph import StateGraph, START, END  
from typing_extensions import TypedDict #used to define state sche,a
from IPython.display import Image


#defining state
class State(TypedDict):
    count: int #ehat kind of data is used in my LangGraph


#Defining node
def increment (state: State):
    return {"count": state["count"]+1}

#creating the graph
graph = StateGraph(State)
#adding the node
graph.add_node("increment", increment)
#setting entry point
graph.set_entry_point("increment")
#setting end point
graph.add_edge("increment", END)
#COMPiling the graph
app=graph.compile()

Image(graph.get_graph().draw_png())
#running the graph, intializing the starrting state with 0 and storing it in result
result = app.invoke({'count':5})
#printing the result
print(result)