from tkinter import *

def button_clicked():
    data = my_entry.get()
    my_label.config(text=data)

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

my_label = Label(text="I am a label", font=("Arial",24,))
my_label.grid(row=0,column=0)

my_entry = Entry(width=10)
my_entry.grid(row=2, column=3)


my_button = Button(text="click me",command=button_clicked)
my_button.grid(row=1, column=1)  


second_button = Button(text="button_2")
second_button.grid(row=0, column=2)


window.mainloop()