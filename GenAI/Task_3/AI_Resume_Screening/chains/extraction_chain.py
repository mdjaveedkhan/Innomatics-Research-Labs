import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.extraction_prompt import extraction_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

def extraction_chain(resume):
    chain = extraction_prompt | llm | parser
    return chain.invoke({"resume": resume})