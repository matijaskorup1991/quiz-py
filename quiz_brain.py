class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        user_answer = input(
            f"Q. {self.question_number}: {self.question_list[self.question_number].text}")
        self.question_number += 1
