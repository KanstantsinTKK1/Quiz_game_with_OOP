class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        while current_answer != 'true' and current_answer != 'false':
            print("You didn't type the word 'true' or 'false' correctly.")
            current_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(current_question.answer, current_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, true_answer, user_answer):
        if user_answer == true_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are not right!")
        print(f"The correct answer was: {true_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")