from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item['question'],item['correct_answer'])
    question_bank.append(new_question)


# for item in question_bank:
#    print(item.text,item.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print("\n")

print("You have completed the quiz.")
print(f"You final score was: {quiz.score}/{quiz.question_number}")