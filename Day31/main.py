from tkinter import *
import pandas
import random

current_card = {}
data_dict = {}

try:
    data = pandas.read_csv(filepath_or_buffer="./data/words_to_learn.csv", encoding="utf-8")
except FileNotFoundError:
    original_data = pandas.read_csv(filepath_or_buffer="./data/french_words.csv", encoding="utf-8")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")




def next():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    print(current_card["French"])

    canvas.itemconfig(canvas_iamge, image=card_front_img)
    canvas.itemconfig(lang_label, text="French")
    canvas.itemconfig(word_label, text=current_card["French"])

    timer = window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(canvas_iamge, image=card_back_img)
    canvas.itemconfig(lang_label, text="English")
    canvas.itemconfig(word_label, text=current_card["English"])

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next()



#Window Setup

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, width=900, height=900, padx=50, pady=50)

timer = window.after(3000,func=flip_card)



card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_iamge = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
x_button_image = PhotoImage(file="./images/wrong.png")
tick_button_image = PhotoImage(file="./images/right.png")

right_button = Button(image=tick_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=x_button_image, highlightthickness=0, command=next)
wrong_button.grid(row=1, column=0)

#Labels

lang_label = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 253, font=("Arial", 60, "bold"))


next()

window.mainloop()


