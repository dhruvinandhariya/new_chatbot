from flask import Flask, jsonify, request
import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Femme Focus Chatbot', response.data)

    def test_chat_route(self):
        response = self.client.get('/chat')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ask me anything related to your health', response.data)

    def test_generate_response(self):
        response = self.client.post('/generate', json={'user_input': 'What services are available?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.get_json())

    def test_scrape_website(self):
        response = self.client.get('/scrape')
        self.assertEqual(response.status_code, 200)
        self.assertIn('website_content', response.get_json())

if __name__ == '__main__':
    unittest.main()
