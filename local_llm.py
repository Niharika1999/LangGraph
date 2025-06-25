# local_llm.py
from langgraph.graph import Graph

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import json

local_llm = "phi3"
llm = ChatOllama(model=local_llm, temperature=0.1)

def Agent(query):
    template = """    Question: {query} Let's think step by step.
        your output format is filename:"" and  content:""
        make sure your output is right json"""
    
    prompt = PromptTemplate(template=template, input_variables=["query"])
    format_instructions = prompt.format_prompt(query=query)
    output = prompt | llm | StrOutputParser()
    return output.invoke(format_instructions.to_string())

def Tool(input):
    print("Tool Stage input:" + input)
    # Parse the JSON input
    data = json.loads(input)
    # Extract the "content" and "filename" parts
    content = data.get("content", "")
    filename = data.get("filename", "output.md")
    # Write the content to the specified filename
    with open(filename, 'w') as file:
        file.write(content)
    return input


# Define a Langchain graph
workflow = Graph()

workflow.add_node("agent", Agent)
workflow.add_node("tool", Tool)

workflow.add_edge('agent', 'tool')

workflow.set_entry_point("agent")
workflow.set_finish_point("tool")

app = workflow.compile()

app.invoke("write an article, content is startup.md ")