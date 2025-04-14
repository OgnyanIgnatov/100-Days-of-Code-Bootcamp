from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
CHECKMARK = "✓"
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps=1
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_min=SHORT_BREAK_MIN*60
    long_break_min=LONG_BREAK_MIN*60
    
    if reps % 2==1:
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_sec)
    elif reps%8==0:
        timer_label.config(fg=RED, text="Long Break")
        count_down(long_break_min)
    elif reps%2==0:
        timer_label.config(fg=PINK, text="Short Break")
        count_down(short_break_min)
    
    reps+=1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec == 0 or count_sec<10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_seesions = math.floor(reps/2)
        for _ in range(work_seesions):
            marks+=CHECKMARK
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodorro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,35,"bold"))
timer_label.grid(row=0,column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(width= 10, text="Start", bg="white", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(width=10, text="Reset", bg="white",command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(text="", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)




window.mainloop()