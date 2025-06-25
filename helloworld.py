from langgraph.graph import Graph

def function1(input_1):
    return input_1 + " Hello "
def function2(input_2):
    return input_2+ "world"

# Create a graph
graph = Graph()
graph.add_node("function1", function1)
graph.add_node("function2", function2)

# Add edges between nodes
graph.add_edge("function1", "function2")
# Set entry and finish points
graph.set_entry_point("function1")
graph.set_finish_point("function2")

app = graph.compile()

print(app.invoke("langgraph: "))