class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.true_answer = 0

    def still_has_question(self):
        return len(self.question_list) - 1 >= self.question_number

    def next_question(self):
        user_answer = input(
            f"Q. {self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)")

        self.check_answer(
            user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.true_answer += 1
            print("Answer is correct! ")
        else:
            print("Wrong! ")
        print(f"score {self.question_number + 1} / {self.true_answer}")
