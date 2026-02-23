from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import  TavilySearch
# from langsmith import traceable
load_dotenv()

tavily=TavilyClient()
def main_old():
    print("Hello from langchain-course!")
    information = "Elon Musk is a business magnate and investor. He is the founder and CEO of SpaceX, and the CEO of Tesla, Inc. He has also been involved in several other ventures, including Neuralink and The Boring Company."
    summery_template = """
    given the information {information} about a person i want you to create:
    1. a short summery
    2. two intersting facts about them
    """

    summery_prompt_template= PromptTemplate(
        input_variables=["information"],
        template=summery_template
    )
    llm = ChatOllama(temperature=0,model="llama3")
    chain = summery_prompt_template | llm
    reponse = chain.invoke(input={"information": information})
    print(reponse.content)

@tool
def search(query: str) -> str:
    """Tool that searches over internet 
    Args:
        query: search query for
    Returns:
        search result"""
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm_tool = ChatOllama(temperature=0,model="qwen3")
tools = [TavilySearch()]
agent = create_agent(model=llm_tool, tools=tools)
def main():
    print("Hello from main!")
    result= agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")]})
    print(result)
if __name__ == "__main__":
    main()
