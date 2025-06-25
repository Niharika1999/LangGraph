from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

# Step 1: Define the state schema
class State(TypedDict):
    count: int

# Step 2: Create a node that increments the count
def increment_node(state: State) -> dict:
    new_count = state["count"] + 1
    print(f"Incrementing count: {state['count']} → {new_count}")
    return {"count": new_count}

# Step 3: Build the graph
graph = StateGraph(State)
graph.add_node("increment", increment_node)

# Connect the flow: START → increment → END
graph.set_entry_point("increment")
graph.add_edge("increment", END)

# Step 4: Compile and run
app = graph.compile()

# Step 5: Execute with initial state
initial_state = {"count": 0}
result = app.invoke(initial_state)

print("\nFinal Output:")
print(result)
