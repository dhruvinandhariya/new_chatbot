from flask import Flask, request, jsonify
import os
import requests
from bs4 import BeautifulSoup
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load API key
os.environ['GROQ_API_KEY'] = "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"
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful and friendly chatbot. Answer the user's question in a clear and concise manner.
    Question: {input}
    """
)

# Initialize Flask app
app = Flask(__name__)
TARGET_WEBSITE_URL = os.getenv("TARGET_WEBSITE_URL", "https://example.com/")

# Function to scrape website content
def scrape_website():
    response = requests.get(TARGET_WEBSITE_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return " ".join(paragraphs)
    return ""

# Function to check if the answer is available in website content
def search_website(content, query):
    if query.lower() in content.lower():
        return "I found some information on the website: " + content[:500] + "..."
    return None

@app.route("/get_response", methods=["post"])
def get_response():
    data = request.get_json()
    user_input = data.get("user_input")
    if user_input:
        website_content = scrape_website()
        result = search_website(website_content, user_input)

        if result:
            return jsonify({"response": result})

        # If no relevant content is found, ask the LLM
        formatted_prompt = prompt.format(input=user_input)
        result = llm.invoke(formatted_prompt)
        response = result.content
        return jsonify({"response": response})

    return jsonify({"response": "No input provided!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
