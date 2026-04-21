from langchain_core.prompts import ChatPromptTemplate

explanation_prompt = ChatPromptTemplate.from_template("""
Explain candidate score in simple terms in 2-3 lines.

Score: {score}
Match Data: {match_result}
Resume Info: {extracted_info}

Rules:
- 2 to 3 sentences
- simple English
- no JSON or code

Answer:
""")