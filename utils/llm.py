from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import re
# This loads the hidden variables from your .env file
load_dotenv()

# Now os.getenv looks for the NAME of the variable, not the value itself!
GROQ_API_KEY = "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"

def get_llm():
    # Print the first 10 characters to see WHICH key is loaded
    print(f">>> DEBUG KEY: {str(GROQ_API_KEY)[:10]}...") 
    
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant",
        temperature=0.7
    )
def generate_response_hash(prompt, context):
    llm = get_llm()

    full_prompt = f"""
You are a smart, helpful assistant.

Answer the user's question directly in a natural way.
Do not mention the website name, source name, confidence, scraped data, or whether data is available or unavailable.
Do not say things like "according to the website", "the website says", "data is available", or "data is not available".
If the information is missing from the provided context, give a brief helpful answer without mentioning the website or missing website data.
Keep the answer focused on the user's question.

Website Content:
{context}

User Question:
{prompt}
"""

    try:
        messages = [HumanMessage(content=full_prompt)]
        response = llm.invoke(messages)
        cleaned_response = response.content.strip()
        cleaned_response = re.sub(
            r"(?im)^.*\b(data|information)\s+is\s+(available|not available|unavailable).*$",
            "",
            cleaned_response,
        )
        cleaned_response = re.sub(
            r"(?im)^.*\b(source|website)\b.*$",
            "",
            cleaned_response,
        )
        cleaned_response = re.sub(r"\n{3,}", "\n\n", cleaned_response).strip()
        return cleaned_response or "I could not find a clear answer."

    except Exception as e:
        print(">>> LLM ERROR:", str(e))
        return "Sorry, something went wrong while generating the response."
