from flask import Blueprint, render_template, request, jsonify
from utils.scraper import scrape_website
from utils.llm import generate_response_hash as generate_response

main = Blueprint('main', __name__)  # Matches __init__.py registration

@main.route('/')
def home():
    return render_template('chat.html')

@main.route('/chat', methods=['POST'])
def chat():
    try:
        print(">>> Chat endpoint hit")

        user_input = request.json.get('input')
        print(">>> User input:", user_input)

        if not user_input:
            return jsonify({"answer": "No input provided"}), 400

        # --- DEBUGGING SHORTCUT ---
        # If you want to isolate and test frontend → backend:
        # response = f"Echo test: {user_input}"
        # return jsonify({"answer": response})

        website_content = scrape_website()
        print(">>> Website content scraped")

        response = generate_response(user_input, website_content)
        print(">>> Response generated:", response)

        return jsonify({"answer": response})

    except Exception as e:
        print(">>> ERROR:", str(e))
        return jsonify({"answer": "Something went wrong on the server."}), 500

@main.route('/refresh', methods=['POST'])
def refresh():
    print(">>> Refresh endpoint called")
    return jsonify({"message": "Website content refreshed"}), 200
