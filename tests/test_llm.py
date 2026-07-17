import unittest
from utils.llm import generate_response

class TestLLMFunctions(unittest.TestCase):

    def test_generate_response_valid_input(self):
        user_input = "What is machine learning?"
        response = generate_response(user_input)
        self.assertIn("response", response)
        self.assertIn("source", response)
        self.assertIn("confidence", response)

    def test_generate_response_technical_question(self):
        user_input = "Explain deep learning."
        response = generate_response(user_input)
        self.assertIn("response", response)
        self.assertIn("source", response)
        self.assertIn("confidence", response)

    def test_generate_response_invalid_input(self):
        user_input = ""
        response = generate_response(user_input)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()