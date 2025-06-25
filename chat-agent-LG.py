#chat-agent-LG.py
#conversational agent using LangGraph
# from langgraph.graph import StateGraph, START, END
# from typing_extensions import TypedDict
from langchain import PromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI as MistralLLM
from langgraph.graph import Agent

#initializing the mistral API key
llm = MistralLLM(model_name="mistral-small", temperature=0.7)

template = PromptTemplate(
    input = ["question"],
    template = "You are a helpful assistant. Your task is to answer the question {question}."
)

agent = Agent(llm=llm, prompt_template=template)  #“graph” is being assembled for you behind the scenes by the Agent API

response = agent.run({"question": "What's the latest version of python?"})
print(response)