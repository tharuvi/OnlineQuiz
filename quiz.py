class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
 
    def take_quiz(self):
        # Go through each question and check the user's answer
        for question, correct_answer in self.questions.items():
            answer = input(f"{question}: ")
            if self.validate_answer(answer, correct_answer):
                self.score += 1
        return self.score
 
    def validate_answer(self, answer, correct_answer):
        # Check if the answer is correct (ignoring case)
        return answer.strip().lower() == correct_answer.strip().lower()
 
    def get_score(self):
        # Return the current score
        return self.score