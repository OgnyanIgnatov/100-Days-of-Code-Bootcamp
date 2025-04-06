import random

class Quizz_Brain: 
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def check_amswer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else: 
            print("You are wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current.question} True or False?: ")
        self.check_amswer(answer, current.answer)
        

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    
