from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
# from langsmith import traceable
load_dotenv()

def main():
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

if __name__ == "__main__":
    main()
