from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")  
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="Question text",
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"),
                                                width=280)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)

        true_image = PhotoImage(file="./Day34/images/true.png")
        false_image = PhotoImage(file="./Day34/images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check_button)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_check_button)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text="End of Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_check_button(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)

    def false_check_button(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="lightgreen")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.change_question)

    def change_question(self):
        self.canvas.config(bg="white")
        self.get_next_question()

        

