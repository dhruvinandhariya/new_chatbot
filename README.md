# Flask Chatbot

This project is a Flask-based web application for interacting with a chatbot that can answer questions using scraped website content, technical concepts, and general knowledge.

## Project Structure

```
flask-chatbot
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application routes
│   ├── templates             # Contains HTML templates
│   │   ├── base.html        # Base template for all pages
│   │   ├── chat.html        # Chat interface template
│   └── static               # Contains static files
│       ├── css
│       │   └── styles.css    # CSS styles for the application
│       └── js
│           └── scripts.js    # JavaScript for client-side interactivity
├── utils                    # Contains utility modules
│   ├── scraper.py           # Functions for scraping website content
│   ├── llm.py               # Functions for interacting with the language model
│   └── helpers.py           # Utility functions for various tasks
├── tests                    # Contains unit tests
│   ├── test_routes.py       # Tests for application routes
│   ├── test_scraper.py      # Tests for scraping functions
│   └── test_llm.py          # Tests for language model functions
├── requirements.txt         # Lists project dependencies
├── config.py                # Configuration settings for the application
├── run.py                   # Entry point for running the application
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-chatbot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the application:**
   - Update the `config.py` file with necessary API keys and settings.

5. **Run the application:**
   ```
   python run.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Usage

- Type your questions in the chat interface to receive responses from the chatbot.
- The chatbot can provide information about the configured website, technical concepts, and general knowledge.

## Testing

To run the tests, use the following command:
```
pytest
```

This will execute all unit tests in the `tests` directory to ensure the application functions as expected.
