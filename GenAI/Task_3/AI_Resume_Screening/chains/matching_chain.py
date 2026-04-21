from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from prompts.matching_prompt import matching_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

def matching_chain(extracted_info, job_description):
    chain = matching_prompt | llm | parser

    return chain.invoke({
        "extracted_info": extracted_info,   # ✅ MUST MATCH PROMPT
        "job_description": job_description   # ✅ MUST MATCH PROMPT
    })