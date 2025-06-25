#conditional_lg.py
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

#Defining my state
class State(TypedDict):
   count : int 

#Defining node 1 - actual operation - increment
def increment (state:State):
    return{"count": state["count"]+1}

#Defining  node 2 - conditions so using loops
def if_else (state: State) -> str:
    return "<3" if state["count"]<3 else "is 3"

#defining state graph
graph = StateGraph(State)
#adding node
graph.add_node("increment", increment)

#adding conditional edges
##checks runs till the count is 3
graph.add_conditional_edges("increment", if_else,{
    "<3": "increment",
    "is 3": END
})

#adding entry point
graph.set_entry_point("increment")

#compile
app = graph.compile()

#executing and printing the result
# intial_state = {"count": 1}
print(app.invoke({"count": 1}))