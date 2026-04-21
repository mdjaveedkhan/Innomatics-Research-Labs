import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.scoring_prompt import scoring_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

def scoring_chain(match_data):
    chain = scoring_prompt | llm | parser
    return chain.invoke({"match_data": match_data})