import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.explanation_prompt import explanation_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

def explanation_chain(score, match_result, extracted_info):
    chain = explanation_prompt | llm | parser
    return chain.invoke({
        "score": score,
        "match_result": match_result,
        "extracted_info": extracted_info
    })