Here’s a list of **important LangGraph keywords (classes, functions, and concepts)** along with a short explanation of what each one does — perfect for understanding or writing your own LangGraph programs.

---

## 🔑 **Essential LangGraph Keywords & Functions**

| **Keyword / Function**                      | **What It Does**                                                               |
| ------------------------------------------- | ------------------------------------------------------------------------------ |
| `StateGraph`                                | Main class used to build a graph of nodes (functions) and flow between them.   |
| `TypedDict` / `Pydantic`                    | Used to define the **state schema** — shared structured data across nodes.     |
| `START` / `END`                             | Special constants marking the start and end of a graph.                        |
| `add_node(name, fn)`                        | Adds a node (a function that operates on state) to the graph.                  |
| `add_edge(from_node, to_node)`              | Adds a **direct connection** between nodes.                                    |
| `add_conditional_edges(node, fn, branches)` | Adds **branching logic** to decide the next step based on state.               |
| `set_entry_point("node_name")`              | Sets the node where execution starts.                                          |
| `compile()`                                 | Converts the graph into a **runnable app**.                                    |
| `invoke(input_state)`                       | Runs the compiled graph using an initial state (like a dictionary).            |
| `ToolNode(fn)`                              | Wraps a tool or external function so it can be added as a node.                |
| `stream(input_state)`                       | Runs the graph and **yields intermediate updates**, useful for streaming UIs.  |
| `@tool` (from LangChain)                    | Decorator to turn a function into a tool that can be used in LangGraph agents. |
| `create_react_agent()`                      | Prebuilt agent pattern that lets an LLM reason, act, and react using tools.    |

---

## 🧩 Categories by Purpose

### 🧠 **Graph Structure**

| Keyword                 | Use Case                 |
| ----------------------- | ------------------------ |
| `StateGraph`            | Build the overall graph  |
| `add_node`              | Define what steps to run |
| `add_edge`              | Define linear flows      |
| `add_conditional_edges` | Add logic/loops/branches |
| `START`, `END`          | Entry and exit points    |
| `set_entry_point`       | Where to begin execution |

---

### 💾 **State Management**

| Keyword        | Purpose                               |
| -------------- | ------------------------------------- |
| `TypedDict`    | Define shape and type of the state    |
| `state["key"]` | Access or modify state in a node      |
| Return `{...}` | Nodes return partial updates to state |

---

### 🚀 **Execution**

| Keyword     | Purpose                     |
| ----------- | --------------------------- |
| `compile()` | Make the graph runnable     |
| `invoke()`  | Run the graph with input    |
| `stream()`  | Stream intermediate results |

---

### 🔧 **Tools & Agents**

| Keyword                | Purpose                              |
| ---------------------- | ------------------------------------ |
| `ToolNode`             | Add external logic or API tools      |
| `@tool` (LangChain)    | Convert Python functions into tools  |
| `create_react_agent()` | Build reasoning LLM + tool workflows |

---

## ✅ Example Usage for Each

```python
# Define state
class State(TypedDict):
    user_input: str
    result: str

# Define a node
def echo(state: State):
    return {"result": state["user_input"]}

# Create graph
g = StateGraph(State)
g.add_node("echo", echo)
g.set_entry_point("echo")
g.add_edge("echo", END)

# Run
app = g.compile()
print(app.invoke({"user_input": "Hello!"}))  # Output: {'user_input': 'Hello!', 'result': 'Hello!'}
```

---


