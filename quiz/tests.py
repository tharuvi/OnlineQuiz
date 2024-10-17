import unittest
from unittest.mock import patch
from quiz import Quiz

class TestQuiz(unittest.TestCase):

    def setUp(self):
        # Sample questions for testing
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is 2 + 2?": "4",
            "What is the capital of Spain?": "Madrid"
        }
        self.quiz = Quiz(self.questions)

    @patch('builtins.input', side_effect=['Paris', '4', 'Madrid'])
    def test_all_correct(self, mock_input):
        score = self.quiz.take_quiz()
        self.assertEqual(score, 3)

    @patch('builtins.input', side_effect=['London', '4', 'Barcelona'])
    def test_some_incorrect(self, mock_input):
        score = self.quiz.take_quiz()
        self.assertEqual(score, 1)  # Only the answer to "2 + 2" is correct

    def test_score_initialization(self):
        # Check if the score starts at 0
        self.assertEqual(self.quiz.get_score(), 0)

if __name__ == '__main__':
    unittest.main()
