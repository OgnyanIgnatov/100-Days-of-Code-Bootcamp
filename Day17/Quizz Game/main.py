from question_model import Question
from data import question_data
from quiz_brain import Quizz_Brain

question_bank = list()

for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quizz = Quizz_Brain(question_bank)

while quizz.still_has_question():
    quizz.next_question()

print("You have completed the Quizz!")
print(f"Your score is: {quizz.score}/{quizz.question_number}")